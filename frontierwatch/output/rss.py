"""RSS feed generator for Frontier Watch."""

from __future__ import annotations

import json
import logging
import re
from datetime import date, datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree, indent

import markdown

logger = logging.getLogger(__name__)

DOCS_DIR = Path(__file__).resolve().parent.parent.parent / "docs"
FEED_DATA_FILE = DOCS_DIR / "feed_data.json"
FEED_XML_FILE = DOCS_DIR / "feed.xml"
MAX_ITEMS = 50

FEED_TITLE = "Frontier Watch"
FEED_DESCRIPTION = (
    "Personal research briefings across biotech, computing & AI, economics, "
    "energy, monetary policy, and securities regulation."
)
FEED_URL = "https://unsubject.github.io/frontierwatch/"
FEED_XML_URL = "https://unsubject.github.io/frontierwatch/feed.xml"

# Category display names
CATEGORY_NAMES = {
    "biotech": "Biotech",
    "computing-ai": "Computing & AI",
    "economics": "Economics & Behavioural Science",
    "energy": "Energy",
    "monetary-policy": "Monetary Policy",
    "securities-futures": "Securities & Futures",
}


class FeedManager:
    """Manages the RSS feed data store and XML generation."""

    def __init__(self):
        self.items: list[dict] = self._load()

    def _load(self) -> list[dict]:
        if FEED_DATA_FILE.exists():
            return json.loads(FEED_DATA_FILE.read_text())
        return []

    def _save(self) -> None:
        DOCS_DIR.mkdir(parents=True, exist_ok=True)
        FEED_DATA_FILE.write_text(json.dumps(self.items, indent=2, ensure_ascii=False))

    def add_entry(
        self,
        *,
        title: str,
        slug: str,
        content_md: str,
        notion_url: str,
        pub_date: date | None = None,
    ) -> None:
        """Add a new briefing entry to the feed."""
        today = pub_date or date.today()
        guid = f"{slug}-{today.isoformat()}"

        # Remove duplicate if re-running same day
        self.items = [item for item in self.items if item["guid"] != guid]

        summary = _extract_summary(content_md)
        content_html = _md_to_html(content_md)

        entry = {
            "title": title,
            "guid": guid,
            "category": CATEGORY_NAMES.get(slug, slug),
            "link": notion_url,
            "summary": summary,
            "content_html": content_html,
            "pub_date": datetime(
                today.year, today.month, today.day,
                8, 0, 0, tzinfo=timezone.utc,
            ).isoformat(),
        }

        self.items.insert(0, entry)
        self.items = self.items[:MAX_ITEMS]

        self._save()
        logger.info("Added RSS entry: %s (guid=%s)", title, guid)

    def generate_feed(self) -> Path:
        """Write docs/feed.xml from the current item list."""
        rss = Element("rss", version="2.0")
        rss.set("xmlns:content", "http://purl.org/rss/1.0/modules/content/")
        rss.set("xmlns:atom", "http://www.w3.org/2005/Atom")

        channel = SubElement(rss, "channel")
        SubElement(channel, "title").text = FEED_TITLE
        SubElement(channel, "link").text = FEED_URL
        SubElement(channel, "description").text = FEED_DESCRIPTION

        atom_link = SubElement(channel, "atom:link")
        atom_link.set("href", FEED_XML_URL)
        atom_link.set("rel", "self")
        atom_link.set("type", "application/rss+xml")

        now = format_datetime(datetime.now(timezone.utc))
        SubElement(channel, "lastBuildDate").text = now

        for item_data in self.items:
            item = SubElement(channel, "item")
            SubElement(item, "title").text = item_data["title"]
            SubElement(item, "link").text = item_data.get("link", "")

            guid_el = SubElement(item, "guid")
            guid_el.set("isPermaLink", "false")
            guid_el.text = item_data["guid"]

            pub_dt = datetime.fromisoformat(item_data["pub_date"])
            SubElement(item, "pubDate").text = format_datetime(pub_dt)
            SubElement(item, "category").text = item_data.get("category", "")
            SubElement(item, "description").text = item_data.get("summary", "")

            content = SubElement(item, "content:encoded")
            content.text = item_data.get("content_html", "")

        indent(rss)
        tree = ElementTree(rss)
        DOCS_DIR.mkdir(parents=True, exist_ok=True)
        tree.write(FEED_XML_FILE, encoding="unicode", xml_declaration=True)

        logger.info("Generated RSS feed: %s (%d items)", FEED_XML_FILE, len(self.items))
        return FEED_XML_FILE


def _extract_summary(md: str, max_len: int = 300) -> str:
    """Extract a plain-text summary from markdown content."""
    # Strip headings, bold markers, links → plain text
    text = re.sub(r"^#{1,3}\s+", "", md, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\n{2,}", "\n", text)

    # Take first non-empty lines up to max_len
    lines = [l.strip() for l in text.split("\n") if l.strip() and not l.strip().startswith("|") and not l.strip().startswith("---")]
    summary = " ".join(lines)
    if len(summary) > max_len:
        summary = summary[:max_len].rsplit(" ", 1)[0] + "..."
    return summary


def _md_to_html(md: str) -> str:
    """Convert markdown to HTML for RSS content:encoded."""
    return markdown.markdown(
        md,
        extensions=["tables", "fenced_code", "nl2br"],
    )
