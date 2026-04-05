"""Securities & Futures Regulatory Watch briefing."""

from __future__ import annotations

from datetime import date, timedelta

from frontierwatch.briefings.base import BaseBriefing

# Official regulator domains
REGULATOR_DOMAINS = [
    "sec.gov",
    "cftc.gov",
    "finra.org",
    "csrc.gov.cn",
    "safe.gov.cn",
    "nafr.gov.cn",
    "esma.europa.eu",
    "ec.europa.eu",
    "fca.org.uk",
    "bankofengland.co.uk",
    "sfc.hk",
    "hkex.com.hk",
]


class SecuritiesFuturesBriefing(BaseBriefing):
    name = "Securities & Futures Regulatory Watch"
    slug = "securities-futures"
    spec_file = "securities-futures-regulatory-watch-spec.md"

    # Notion: page-backed
    notion_parent_id = "33911045-5975-8057-b352-df2f25b8403f"
    notion_parent_type = "page"

    domain_filter = REGULATOR_DOMAINS
    recency = "month"

    def compute_date_range(self, end_date: date | None = None) -> tuple[str, date, date]:
        """Override: 14-day rolling window for fortnightly briefing."""
        end = end_date or date.today()
        start = end - timedelta(days=14)
        display = f"{start.strftime('%b %d')} – {end.strftime('%b %d, %Y')}"
        return display, start, end

    def get_research_queries(self, date_range: str) -> list[dict]:
        base = {
            "domain_filter": self.domain_filter,
            "recency": "month",
            "system_prompt": (
                "You are a securities regulation analyst. Return ONLY information from "
                "official regulatory sources. Include specific rule numbers, consultation "
                "paper references, and effective dates. No law firm alerts, no industry "
                "commentary, no wire services."
            ),
        }

        return [
            {
                **base,
                "query": (
                    f"SEC, CFTC, and FINRA new rulemaking, rule proposals, market structure "
                    f"changes, enforcement policy shifts, and digital asset regulation "
                    f"during {date_range}."
                ),
            },
            {
                **base,
                "query": (
                    f"CSRC, SAFE, and NAFR securities and futures regulatory actions, "
                    f"new rules, market structure changes, and cross-border coordination "
                    f"during {date_range}."
                ),
            },
            {
                **base,
                "query": (
                    f"ESMA and European Commission securities and derivatives regulation, "
                    f"MiFID updates, EMIR changes, and digital asset frameworks "
                    f"during {date_range}."
                ),
            },
            {
                **base,
                "query": (
                    f"FCA, PRA, SFC Hong Kong, and HKEX regulatory actions, "
                    f"new rulemaking, market structure changes, crypto regulation, "
                    f"and cross-border coordination during {date_range}."
                ),
            },
        ]

    def get_extra_instructions(self) -> str:
        return (
            "CRITICAL: Use ONLY official regulator sources. No law firm client alerts, "
            "no industry commentary, no wire services.\n"
            "Use the hybrid structure: thematic overview (Part A) + jurisdiction detail (Part B).\n"
            "The Quick-Reference Table should only include jurisdictions with material activity.\n"
            "Omit thematic sections (A1-A6) that have no material activity.\n"
            "Every jurisdiction gets the same six subsections in Part B.\n"
            "End with a Source Log listing all official sources consulted with URLs.\n"
            "For properties, include: Item Count (number of material regulatory actions).\n"
            "watchlist_items should be empty — this briefing has no watchlist."
        )
