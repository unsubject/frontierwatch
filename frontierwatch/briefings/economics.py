"""Economics & Behavioural Science Watch briefing."""

from __future__ import annotations

from frontierwatch.briefings.base import BaseBriefing


class EconomicsBriefing(BaseBriefing):
    name = "Economics & Behavioural Science Watch"
    slug = "economics"
    spec_file = "economics-behavioural-science-watch-spec.md"

    # Notion: page-backed (no database)
    notion_parent_id = "33911045-5975-81fa-b71e-e2b3dea7ddff"
    notion_parent_type = "page"

    # Academic sources — constrain Perplexity to scholarly domains
    domain_filter = [
        "nber.org",
        "ssrn.com",
        "doi.org",
        "scholar.google.com",
        "aeaweb.org",
        "restud.com",
        "academic.oup.com",
        "onlinelibrary.wiley.com",
        "journals.sagepub.com",
        "sciencedirect.com",
        "cepr.org",
        "brookings.edu",
    ]
    recency = "week"

    def get_research_queries(self, date_range: str) -> list[dict]:
        base = {
            "domain_filter": self.domain_filter,
            "recency": "week",
            "system_prompt": (
                "You are an academic research assistant. Return only peer-reviewed papers "
                "and working papers with full citation details (authors, year, journal/venue, "
                "DOI or URL). No journalism, no commentary, no op-eds."
            ),
        }
        return [
            {
                **base,
                "query": (
                    f"Recent economics working papers and published articles from NBER, "
                    f"SSRN, AER, QJE, JPE, Econometrica, or Review of Economic Studies "
                    f"during {date_range}. Focus on macroeconomics, institutional economics, "
                    f"political economy, and development economics."
                ),
            },
            {
                **base,
                "query": (
                    f"Recent behavioural economics and behavioural science papers from "
                    f"Psychological Science, Journal of Economic Perspectives, Cognition, "
                    f"Journal of Experimental Psychology during {date_range}. "
                    f"Focus on decision-making, cognitive biases, nudge theory, neuroeconomics."
                ),
            },
            {
                **base,
                "query": (
                    f"Recent financial economics papers from Journal of Finance, JFE, "
                    f"Review of Financial Studies during {date_range}. "
                    f"Cover asset pricing, market microstructure, corporate finance, "
                    f"household finance, and risk."
                ),
            },
            {
                **base,
                "query": (
                    f"Cross-domain papers bridging economics, behavioural science, and "
                    f"financial economics published or posted as working papers during "
                    f"{date_range}. These are the most valuable — look for papers that "
                    f"connect decision-making psychology with market or policy outcomes."
                ),
            },
        ]

    def get_extra_instructions(self) -> str:
        return (
            "Target length: ~2,000+ words.\n"
            "Feature exactly 3-4 papers at equal depth (~400-500 words each).\n"
            "Prioritize cross-domain papers that bridge two or more fields.\n"
            "Every paper MUST have a full citation block with authors, year, journal, DOI.\n"
            "The Opening Frame must be an analytical framing, NOT a summary.\n"
            "The Cross-Paper Synthesis is the most valuable section — invest in it.\n"
            "For watchlist_items, use Paper Log format:\n"
            "- name (paper title), status (Peer-Reviewed/Working Paper/Forthcoming)\n"
            '- additional_fields: authors, year, journal_or_venue, domain, doi_or_url, notes\n'
            "For properties: Paper Count (int), Has Market Signal (bool)."
        )
