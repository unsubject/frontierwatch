"""Computing & AI Watch briefing."""

from __future__ import annotations

from frontierwatch.briefings.base import BaseBriefing


class ComputingAIBriefing(BaseBriefing):
    name = "Computing & AI Watch"
    slug = "computing-ai"
    spec_file = "computing-ai-watch-spec.md"

    # Notion: page-backed (no database)
    notion_parent_id = "33911045-5975-80d4-a56e-d119b8d94658"
    notion_parent_type = "page"

    recency = "week"

    def get_research_queries(self, date_range: str) -> list[dict]:
        return [
            {
                "query": (
                    f"Most significant AI and machine learning developments during {date_range}. "
                    f"Cover foundation models, training and inference advances, AI agents, "
                    f"multimodal models, alignment research, and benchmark shifts. "
                    f"Include company names and ticker symbols where relevant."
                ),
                "recency": "week",
            },
            {
                "query": (
                    f"Quantum computing milestones and breakthroughs during {date_range}. "
                    f"Cover qubit counts, error correction, coherence times, algorithm "
                    f"breakthroughs, and commercial deployments."
                ),
                "recency": "week",
            },
            {
                "query": (
                    f"Recent landmark papers in AI/ML, quantum computing, and computer science "
                    f"from arXiv, NeurIPS, ICML, ICLR, STOC, FOCS, Nature, or Science "
                    f"during {date_range}. Focus on field-shifting results only."
                ),
                "recency": "week",
            },
            {
                "query": (
                    f"AI hardware and chip developments during {date_range}. "
                    f"Cover AI accelerators, neuromorphic computing, and photonic computing "
                    f"advances from NVIDIA, AMD, Intel, Google, startups."
                ),
                "recency": "week",
            },
        ]

    def get_extra_instructions(self) -> str:
        return (
            "Keep the total length to ~1,000-1,500 words.\n"
            "For watchlist_items, each item should include:\n"
            "- name, ticker, status\n"
            '- additional_fields with: domain (string), type (string), stage (string)\n'
            "Use today's date for date_added and last_updated fields.\n"
            "For properties, include: Item Count, Has Landmark Paper (bool), Has Investment Signals (bool)."
        )
