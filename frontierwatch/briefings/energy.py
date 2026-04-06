"""Energy Frontier Briefing."""

from __future__ import annotations

from frontierwatch.briefings.base import BaseBriefing


class EnergyBriefing(BaseBriefing):
    name = "Energy Frontier Briefing"
    slug = "energy"
    spec_file = "energy-watch-spec-v2.md"

    # Notion: database-backed
    notion_parent_id = "d5b27811-e041-4daf-be72-3f381509e01e"
    notion_parent_type = "database"
    notion_watchlist_db_id = "a0e10c72-c509-4b77-aeeb-c0a54e00c805"

    recency = "month"

    def get_research_queries(self, date_range: str) -> list[dict]:
        return [
            {
                "query": (
                    f"Frontier energy technology developments and breakthroughs during "
                    f"{date_range}. Cover electricity and grid innovations, nuclear fission "
                    f"and fusion, renewables and energy storage, and oil & gas technology. "
                    f"Focus on genuinely disruptive potential, not incremental improvements."
                ),
                "recency": "month",
            },
            {
                "query": (
                    f"Recent peer-reviewed energy science papers published in Nature Energy, "
                    f"Joule, Science, Science Advances, Energy & Environmental Science, "
                    f"or Advanced Energy Materials during {date_range}. "
                    f"Focus on novel mechanisms and step-change performance improvements."
                ),
                "recency": "month",
            },
            {
                "query": (
                    f"DOE, IEA, and EIA energy policy announcements, funding programs, "
                    f"and strategy shifts during {date_range}. Include IRA tax credit "
                    f"developments and permitting milestones."
                ),
                "recency": "month",
            },
            {
                "query": (
                    f"Energy technology startup funding, IPOs, and corporate investments "
                    f"in clean energy and grid technology during {date_range}. "
                    f"Include company names, ticker symbols, and deal sizes."
                ),
                "recency": "month",
            },
        ]

    def get_extra_instructions(self) -> str:
        return (
            "Target read time: 15-20 minutes.\n"
            "For the properties field, include:\n"
            '- "Issue": integer issue number (use 1 if unknown)\n'
            '- "Date Range": the coverage period string\n'
            '- "Date Published": today\'s date as YYYY-MM-DD\n'
            '- "Item Count": number of frontier development writeups\n'
            '- "Has Policy": boolean, true if Policy & Regulation section is included\n'
            '- "Theme": one-line thematic thread\n'
            "\n"
            "For watchlist_items, each item should include:\n"
            "- name, ticker, status\n"
            '- additional_fields with: sector (string), stage (string)\n'
            "Use today's date for date_added and last_updated fields."
        )
