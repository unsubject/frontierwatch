"""Claude Sonnet synthesizer for briefing generation."""

from __future__ import annotations

import json
import logging
import os

import anthropic

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 16_000


class Synthesizer:
    """Uses Claude Sonnet to turn raw research into a structured briefing."""

    def __init__(self, model: str = DEFAULT_MODEL):
        self.client = anthropic.Anthropic()
        self.model = model

    def synthesize(
        self,
        spec_content: str,
        research_data: list[dict],
        extra_instructions: str = "",
        date_range: str = "",
    ) -> dict:
        """Produce a briefing from the spec and research data.

        Returns a dict with keys:
        - ``title``: str
        - ``date_range``: str
        - ``theme``: str (one-line theme or empty)
        - ``content``: str (full markdown briefing body)
        - ``watchlist_items``: list[dict] (items for watchlist DB, may be empty)
        - ``properties``: dict (extra DB properties like item_count, checkboxes)
        """
        research_text = self._format_research(research_data)

        system_prompt = (
            "You are an expert analyst producing a personal research briefing. "
            "Follow the specification document EXACTLY for structure, tone, depth, "
            "and formatting. Your output must be valid JSON matching the schema below.\n\n"
            "## Output JSON Schema\n"
            "```json\n"
            "{\n"
            '  "title": "string — briefing title per spec",\n'
            '  "date_range": "string — coverage window e.g. Mar 23 – Apr 6, 2026",\n'
            '  "theme": "string — one-line thematic thread (empty string if not applicable)",\n'
            '  "content": "string — the FULL briefing body in Markdown, following the spec template exactly",\n'
            '  "watchlist_items": [\n'
            "    {\n"
            '      "name": "string",\n'
            '      "ticker": "string or empty",\n'
            '      "status": "string — one-line status",\n'
            '      "additional_fields": {}\n'
            "    }\n"
            "  ],\n"
            '  "properties": {}\n'
            "}\n"
            "```\n\n"
            "Rules:\n"
            "- The `content` field must contain the COMPLETE briefing as Markdown.\n"
            "- Fill `watchlist_items` with any items that should be added/updated in the watchlist.\n"
            "- Fill `properties` with database-specific fields described in the spec (item_count, checkboxes, etc.).\n"
            "- Use ONLY information from the provided research data. Do not fabricate sources.\n"
            "- If research data is insufficient for a section, note it honestly rather than inventing content.\n"
        )

        user_prompt = (
            f"## Specification Document\n\n{spec_content}\n\n"
            f"## Coverage Period\n\n{date_range}\n\n"
            f"## Research Data\n\n{research_text}\n\n"
        )
        if extra_instructions:
            user_prompt += f"## Additional Instructions\n\n{extra_instructions}\n\n"

        user_prompt += (
            "Now produce the briefing as a single JSON object. "
            "Return ONLY valid JSON — no markdown fences, no commentary outside the JSON."
        )

        logger.info("Synthesizing briefing with %s (%d chars research)", self.model, len(research_text))

        message = self.client.messages.create(
            model=self.model,
            max_tokens=MAX_TOKENS,
            messages=[{"role": "user", "content": user_prompt}],
            system=system_prompt,
        )

        raw = message.content[0].text.strip()
        # Strip markdown fences if present
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1]
            if raw.endswith("```"):
                raw = raw[: raw.rfind("```")]
            raw = raw.strip()

        return json.loads(raw)

    @staticmethod
    def _format_research(research_data: list[dict]) -> str:
        parts = []
        for i, item in enumerate(research_data, 1):
            parts.append(f"### Research Result {i}\n")
            parts.append(item.get("content", ""))
            citations = item.get("citations", [])
            if citations:
                parts.append("\n**Sources:**")
                for url in citations:
                    parts.append(f"- {url}")
            parts.append("\n---\n")
        return "\n".join(parts)
