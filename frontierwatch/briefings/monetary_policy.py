"""Weekly Central Bank Monetary Policy Briefing."""

from __future__ import annotations

from frontierwatch.briefings.base import BaseBriefing

# Official central bank domains — Perplexity will be constrained to these
CENTRAL_BANK_DOMAINS = [
    "federalreserve.gov",
    "pbc.gov.cn",
    "ecb.europa.eu",
    "boj.or.jp",
    "rbi.org.in",
    "bankofengland.co.uk",
    "bankofcanada.ca",
    "bcb.gov.br",
    "bok.or.kr",
    "rba.gov.au",
    "tcmb.gov.tr",
    "snb.ch",
    "resbank.co.za",
]


class MonetaryPolicyBriefing(BaseBriefing):
    name = "Weekly Central Bank Monetary Policy Briefing"
    slug = "monetary-policy"
    spec_file = "monetary-policy-briefing-spec.md"

    # Notion: page-backed
    notion_parent_id = "33911045-5975-801d-87c3-f743c78200ab"
    notion_parent_type = "page"

    domain_filter = CENTRAL_BANK_DOMAINS
    recency = "week"

    def get_research_queries(self, date_range: str) -> list[dict]:
        base = {
            "domain_filter": self.domain_filter,
            "recency": "week",
            "system_prompt": (
                "You are a central bank policy analyst. Return ONLY information from "
                "official central bank sources. Include specific dates, rate levels, "
                "and direct quotes from official statements. No wire service reporting, "
                "no analyst commentary."
            ),
        }

        # Split into regional groups to get better coverage
        return [
            {
                **base,
                "query": (
                    f"Federal Reserve, European Central Bank, and Bank of England "
                    f"monetary policy actions, rate decisions, forward guidance, "
                    f"open market operations, speeches, and publications "
                    f"during {date_range}."
                ),
            },
            {
                **base,
                "query": (
                    f"People's Bank of China, Bank of Japan, and Reserve Bank of India "
                    f"monetary policy actions, rate decisions, forward guidance, "
                    f"open market operations, FX interventions, and publications "
                    f"during {date_range}."
                ),
            },
            {
                **base,
                "query": (
                    f"Bank of Canada, Banco Central do Brasil, Bank of Korea, "
                    f"and Reserve Bank of Australia monetary policy actions, "
                    f"rate decisions, and forward guidance during {date_range}."
                ),
            },
            {
                **base,
                "query": (
                    f"Central Bank of Turkey, Swiss National Bank, and South African "
                    f"Reserve Bank monetary policy actions, rate decisions, "
                    f"and forward guidance during {date_range}."
                ),
            },
        ]

    def get_extra_instructions(self) -> str:
        return (
            "CRITICAL: Use ONLY official central bank sources. No wire services, "
            "no analyst commentary, no market pricing data.\n"
            "The Quick-Reference Table MUST cover all 13 central banks.\n"
            "Every bank gets the same five subsections even if most say 'Nothing material.'\n"
            "The Cross-Bank Analysis should identify convergence/divergence.\n"
            "End with a Source Log listing all official sources consulted with URLs.\n"
            "For properties, include: Item Count (number of banks with material activity).\n"
            "watchlist_items should be empty — this briefing has no watchlist."
        )
