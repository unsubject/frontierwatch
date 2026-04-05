"""Biotech Frontier Intelligence Report briefing."""

from __future__ import annotations

from frontierwatch.briefings.base import BaseBriefing


class BiotechBriefing(BaseBriefing):
    name = "Biotech Frontier Intelligence Report"
    slug = "biotech"
    spec_file = "biotech-watch-spec.md"

    # Notion: database-backed
    notion_parent_id = "2583c017-68fe-41a3-8c56-65f4afafb875"
    notion_parent_type = "database"
    notion_watchlist_db_id = "0b8d7a5c-679b-4d3e-b950-7ad2b6f3b6f3"

    recency = "month"

    def get_research_queries(self, date_range: str) -> list[dict]:
        return [
            {
                "query": (
                    f"Latest biotech and life sciences breakthroughs, clinical trial results, "
                    f"and FDA/EMA regulatory decisions in the period {date_range}. "
                    f"Cover oncology, neurology, metabolic disease, gene therapy, cell therapy, "
                    f"immunology, rare diseases, and longevity research."
                ),
                "recency": "month",
            },
            {
                "query": (
                    f"Recent peer-reviewed biotech papers with disruptive potential published "
                    f"in Nature, Science, Cell, NEJM, The Lancet, Nature Medicine, "
                    f"Nature Biotechnology, or Science Translational Medicine during {date_range}. "
                    f"Focus on novel mechanisms, step-change efficacy, or paradigm-shifting findings."
                ),
                "recency": "month",
            },
            {
                "query": (
                    f"Biotech venture capital funding rounds, IPOs, M&A deals, and licensing "
                    f"partnerships during {date_range}. Include deal sizes and key investors."
                ),
                "recency": "month",
            },
            {
                "query": (
                    f"FDA and EMA drug approvals, breakthrough therapy designations, fast-track "
                    f"designations, and complete response letters during {date_range}."
                ),
                "recency": "month",
            },
        ]

    def get_extra_instructions(self) -> str:
        return (
            "For the properties field, include:\n"
            '- "Issue": integer issue number (use 1 if unknown)\n'
            '- "Date Range": the coverage period string\n'
            '- "Date Published": today\'s date as YYYY-MM-DD\n'
            '- "Item Count": number of frontier development writeups\n'
            '- "Has Capital Trends": boolean, true if R&D Capital Trends section is included\n'
            '- "Has Regulatory": boolean, true if Regulatory Milestones section is included\n'
            "\n"
            "For watchlist_items, each item should include:\n"
            "- name, ticker, status\n"
            '- additional_fields with: therapeutic_area (list), platform (list), stage (string)\n'
            "Use today's date for date_added and last_updated fields."
        )
