"""Base class for all area briefings."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from datetime import date, timedelta
from pathlib import Path

from frontierwatch.output.notion import NotionClient
from frontierwatch.processing.synthesizer import Synthesizer
from frontierwatch.sources.perplexity import PerplexityClient

logger = logging.getLogger(__name__)

SPECS_DIR = Path(__file__).resolve().parent.parent.parent / "specs"


class BaseBriefing(ABC):
    """Template for an area briefing pipeline: gather → synthesize → publish."""

    name: str = ""
    slug: str = ""
    spec_file: str = ""

    # Notion destination
    notion_parent_id: str = ""
    notion_parent_type: str = "page"  # "page" or "database"
    notion_watchlist_db_id: str | None = None

    # Research config
    domain_filter: list[str] | None = None
    recency: str = "week"

    def __init__(self):
        self._perplexity = None
        self._synthesizer = None
        self._notion = None

    @property
    def perplexity(self) -> PerplexityClient:
        if self._perplexity is None:
            self._perplexity = PerplexityClient()
        return self._perplexity

    @property
    def synthesizer(self) -> Synthesizer:
        if self._synthesizer is None:
            self._synthesizer = Synthesizer()
        return self._synthesizer

    @property
    def notion(self) -> NotionClient:
        if self._notion is None:
            self._notion = NotionClient()
        return self._notion

    # ------------------------------------------------------------------
    # Abstract interface
    # ------------------------------------------------------------------

    @abstractmethod
    def get_research_queries(self, date_range: str) -> list[dict]:
        """Return list of query dicts for Perplexity.

        Each dict must have ``query`` (str) and may include
        ``domain_filter``, ``recency``, ``system_prompt``.
        """

    def get_extra_instructions(self) -> str:
        """Optional extra instructions passed to the synthesizer."""
        return ""

    # ------------------------------------------------------------------
    # Pipeline steps
    # ------------------------------------------------------------------

    def read_spec(self) -> str:
        spec_path = SPECS_DIR / self.spec_file
        return spec_path.read_text()

    def compute_date_range(self, end_date: date | None = None) -> tuple[str, date, date]:
        """Return (display_string, start_date, end_date)."""
        end = end_date or date.today()
        days_back = 14 if self.recency == "month" else 7
        start = end - timedelta(days=days_back)
        display = f"{start.strftime('%b %d')} – {end.strftime('%b %d, %Y')}"
        return display, start, end

    def gather(self, date_range: str) -> list[dict]:
        """Run research queries via Perplexity."""
        queries = self.get_research_queries(date_range)
        logger.info("[%s] Running %d research queries", self.slug, len(queries))
        return self.perplexity.multi_search(queries)

    def synthesize(self, research_data: list[dict], date_range: str) -> dict:
        """Use Claude Sonnet to produce the briefing."""
        spec = self.read_spec()
        return self.synthesizer.synthesize(
            spec_content=spec,
            research_data=research_data,
            extra_instructions=self.get_extra_instructions(),
            date_range=date_range,
        )

    def publish(self, result: dict) -> str:
        """Create a Notion page and optionally upsert watchlist items."""
        url = self.notion.create_briefing_page(
            parent_id=self.notion_parent_id,
            parent_type=self.notion_parent_type,
            title=result["title"],
            markdown=result["content"],
            properties=result.get("properties"),
        )

        # Upsert watchlist items if DB is configured
        if self.notion_watchlist_db_id and result.get("watchlist_items"):
            for item in result["watchlist_items"]:
                self.notion.upsert_watchlist_item(
                    self.notion_watchlist_db_id, item
                )

        return url

    def run(self, end_date: date | None = None) -> str:
        """Execute the full pipeline: gather → synthesize → publish."""
        date_display, start, end = self.compute_date_range(end_date)
        logger.info("[%s] Starting briefing for %s", self.slug, date_display)

        research = self.gather(date_display)
        result = self.synthesize(research, date_display)
        url = self.publish(result)

        logger.info("[%s] Published: %s", self.slug, url)
        return url
