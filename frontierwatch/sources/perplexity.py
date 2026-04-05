"""Perplexity API client for research gathering."""

from __future__ import annotations

import logging
import os

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.perplexity.ai/chat/completions"
DEFAULT_MODEL = "sonar-pro"


class PerplexityClient:
    """Thin wrapper around the Perplexity chat-completions endpoint."""

    def __init__(self, api_key: str | None = None, model: str = DEFAULT_MODEL):
        self.api_key = api_key or os.environ["PERPLEXITY_API_KEY"]
        self.model = model

    def search(
        self,
        query: str,
        *,
        system_prompt: str = "Be precise and comprehensive. Return factual information with sources.",
        domain_filter: list[str] | None = None,
        recency: str = "week",
    ) -> dict:
        """Run a single search query.

        Returns dict with keys: ``content`` (str) and ``citations`` (list[str]).
        """
        payload: dict = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query},
            ],
            "search_recency_filter": recency,
        }
        if domain_filter:
            payload["search_domain_filter"] = domain_filter

        with httpx.Client(timeout=120) as client:
            resp = client.post(
                API_URL,
                json=payload,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
            )
            resp.raise_for_status()

        data = resp.json()
        choice = data["choices"][0]["message"]
        return {
            "content": choice.get("content", ""),
            "citations": data.get("citations", []),
        }

    def multi_search(
        self,
        queries: list[dict],
    ) -> list[dict]:
        """Run multiple search queries sequentially.

        Each entry in *queries* is a dict passed as kwargs to :meth:`search`.
        Returns a list of result dicts in the same order.
        """
        results = []
        for q in queries:
            query_text = q.pop("query")
            logger.info("Perplexity search: %s", query_text[:80])
            result = self.search(query_text, **q)
            results.append(result)
        return results
