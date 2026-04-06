"""Notion API client for publishing briefings."""

from __future__ import annotations

import logging
import os
import re
from datetime import date

import httpx

logger = logging.getLogger(__name__)

NOTION_API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
MAX_BLOCK_TEXT = 2000
BLOCKS_PER_REQUEST = 100


class NotionClient:
    """Publish briefings and manage watchlists via the Notion API."""

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.environ["NOTION_API_KEY"]
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": NOTION_VERSION,
        }

    # ------------------------------------------------------------------
    # Public helpers
    # ------------------------------------------------------------------

    def create_briefing_page(
        self,
        *,
        parent_id: str,
        parent_type: str = "page",
        title: str,
        markdown: str,
        properties: dict | None = None,
    ) -> str:
        """Create a Notion page and return its URL.

        *parent_type* is ``"page"`` or ``"database"``.
        """
        logger.info("Converting markdown to Notion blocks (%d chars)", len(markdown))
        blocks = markdown_to_blocks(markdown)
        logger.info("Converted to %d Notion blocks", len(blocks))

        if parent_type == "database":
            parent = {"database_id": parent_id}
            props = self._build_db_properties(title, properties or {})
        else:
            parent = {"page_id": parent_id}
            props = {"title": [{"text": {"content": title}}]}

        # First request: create page with up to 100 blocks
        first_batch = blocks[:BLOCKS_PER_REQUEST]
        body = {"parent": parent, "properties": props, "children": first_batch}

        timeout = httpx.Timeout(connect=15, read=60, write=30, pool=15)
        with httpx.Client(timeout=timeout, headers=self.headers) as client:
            logger.info("Creating Notion page (batch 1, %d blocks)...", len(first_batch))
            resp = client.post(f"{NOTION_API}/pages", json=body)
            if not resp.is_success:
                logger.error("Notion API error %d: %s", resp.status_code, resp.text[:500])
            resp.raise_for_status()
            page = resp.json()
            page_id = page["id"]
            page_url = page.get("url", "")

            # Append remaining blocks in batches
            remaining = blocks[BLOCKS_PER_REQUEST:]
            batch_num = 2
            while remaining:
                batch = remaining[:BLOCKS_PER_REQUEST]
                remaining = remaining[BLOCKS_PER_REQUEST:]
                logger.info("Appending blocks (batch %d, %d blocks)...", batch_num, len(batch))
                resp = client.patch(
                    f"{NOTION_API}/blocks/{page_id}/children",
                    json={"children": batch},
                )
                if not resp.is_success:
                    logger.error("Notion API error %d: %s", resp.status_code, resp.text[:500])
                resp.raise_for_status()
                batch_num += 1

        logger.info("Created Notion page: %s", page_url)
        return page_url

    def upsert_watchlist_item(
        self,
        database_id: str,
        item: dict,
        title_field: str = "Name",
    ) -> str:
        """Add or update a watchlist entry. Returns the page ID."""
        existing = self._find_by_title(database_id, title_field, item.get("name", ""))

        # Fetch database schema to only send valid properties
        valid_props = self._get_db_properties(database_id)
        props = self._watchlist_item_to_properties(item, title_field)
        # Filter out properties not in the database schema
        if valid_props:
            filtered = {k: v for k, v in props.items() if k in valid_props}
            dropped = set(props.keys()) - set(filtered.keys())
            if dropped:
                logger.warning("Dropped unknown properties for watchlist: %s", dropped)
            props = filtered

        timeout = httpx.Timeout(connect=15, read=60, write=30, pool=15)
        with httpx.Client(timeout=timeout, headers=self.headers) as client:
            if existing:
                page_id = existing
                resp = client.patch(
                    f"{NOTION_API}/pages/{page_id}",
                    json={"properties": props},
                )
                if not resp.is_success:
                    logger.error("Watchlist update error %d: %s", resp.status_code, resp.text[:500])
                resp.raise_for_status()
                logger.info("Updated watchlist item: %s", item.get("name"))
            else:
                body = {
                    "parent": {"database_id": database_id},
                    "properties": props,
                }
                resp = client.post(f"{NOTION_API}/pages", json=body)
                if not resp.is_success:
                    logger.error("Watchlist create error %d: %s", resp.status_code, resp.text[:500])
                resp.raise_for_status()
                page_id = resp.json()["id"]
                logger.info("Created watchlist item: %s", item.get("name"))

        return page_id

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _get_db_properties(self, database_id: str) -> set[str] | None:
        """Fetch the set of property names from a Notion database."""
        try:
            with httpx.Client(timeout=30, headers=self.headers) as client:
                resp = client.get(f"{NOTION_API}/databases/{database_id}")
                resp.raise_for_status()
                schema = resp.json().get("properties", {})
                return set(schema.keys())
        except Exception as exc:
            logger.warning("Could not fetch DB schema for %s: %s", database_id, exc)
            return None

    def _find_by_title(self, database_id: str, title_field: str, title: str) -> str | None:
        """Search a database for an entry matching *title*. Returns page ID or None."""
        body = {
            "filter": {
                "property": title_field,
                "title": {"equals": title},
            },
            "page_size": 1,
        }
        with httpx.Client(timeout=30, headers=self.headers) as client:
            resp = client.post(f"{NOTION_API}/databases/{database_id}/query", json=body)
            resp.raise_for_status()
            results = resp.json().get("results", [])
        return results[0]["id"] if results else None

    @staticmethod
    def _build_db_properties(title: str, extra: dict) -> dict:
        """Build Notion database page properties."""
        props: dict = {
            "Title": {"title": [{"text": {"content": title}}]},
        }
        # Map common property names to Notion property types
        type_map = {
            "Issue": "number",
            "Date Range": "rich_text",
            "Date Published": "date",
            "Item Count": "number",
            "Has Capital Trends": "checkbox",
            "Has Regulatory": "checkbox",
            "Has Policy": "checkbox",
            "Theme": "rich_text",
        }
        for key, value in extra.items():
            ptype = type_map.get(key)
            if ptype == "number" and isinstance(value, (int, float)):
                props[key] = {"number": value}
            elif ptype == "date" and value:
                props[key] = {"date": {"start": str(value)}}
            elif ptype == "checkbox" and isinstance(value, bool):
                props[key] = {"checkbox": value}
            elif ptype == "rich_text":
                props[key] = {"rich_text": [{"text": {"content": str(value)}}]}
        return props

    @staticmethod
    def _watchlist_item_to_properties(item: dict, title_field: str) -> dict:
        """Convert a watchlist item dict to Notion properties."""
        props: dict = {}

        if "name" in item:
            props[title_field] = {"title": [{"text": {"content": item["name"]}}]}

        text_fields = ["Ticker", "Status"]
        for f in text_fields:
            key = f.lower().replace(" ", "_")
            if key in item and item[key]:
                props[f] = {"rich_text": [{"text": {"content": str(item[key])}}]}

        select_fields = ["Sector", "Stage", "Domain", "Type"]
        for f in select_fields:
            key = f.lower()
            if key in item and item[key]:
                props[f] = {"select": {"name": item[key]}}

        multiselect_fields = ["Therapeutic Area", "Platform"]
        for f in multiselect_fields:
            key = f.lower().replace(" ", "_")
            if key in item and item[key]:
                if isinstance(item[key], list):
                    props[f] = {"multi_select": [{"name": v} for v in item[key]]}
                else:
                    props[f] = {"multi_select": [{"name": item[key]}]}

        date_fields = ["Date Added", "Last Updated"]
        for f in date_fields:
            key = f.lower().replace(" ", "_")
            if key in item and item[key]:
                props[f] = {"date": {"start": str(item[key])}}

        # Merge any additional_fields
        additional = item.get("additional_fields", {})
        for k, v in additional.items():
            if k not in props:
                if isinstance(v, bool):
                    props[k] = {"checkbox": v}
                elif isinstance(v, (int, float)):
                    props[k] = {"number": v}
                elif isinstance(v, str):
                    props[k] = {"rich_text": [{"text": {"content": v}}]}

        # Default Last Updated to today
        if "Last Updated" not in props:
            props["Last Updated"] = {"date": {"start": str(date.today())}}

        return props


# ------------------------------------------------------------------
# Markdown → Notion Blocks converter
# ------------------------------------------------------------------

def _parse_rich_text(text: str) -> list[dict]:
    """Parse inline markdown (bold, italic, code, links) into Notion rich_text objects."""
    segments: list[dict] = []
    # Pattern matches: **bold**, *italic*, `code`, [text](url)
    pattern = re.compile(
        r"(\*\*(.+?)\*\*)"           # bold
        r"|(\*(.+?)\*)"              # italic
        r"|(`(.+?)`)"                # inline code
        r"|(\[([^\]]+)\]\(([^)]+)\))" # link
    )
    pos = 0
    for m in pattern.finditer(text):
        # Plain text before this match
        if m.start() > pos:
            plain = text[pos : m.start()]
            if plain:
                segments.extend(_chunk_text(plain, {}))
        if m.group(2):  # bold
            segments.extend(_chunk_text(m.group(2), {"bold": True}))
        elif m.group(4):  # italic
            segments.extend(_chunk_text(m.group(4), {"italic": True}))
        elif m.group(6):  # code
            segments.extend(_chunk_text(m.group(6), {"code": True}))
        elif m.group(8):  # link
            link_text = m.group(9)
            link_url = m.group(10)
            segments.append({
                "type": "text",
                "text": {"content": link_text, "link": {"url": link_url}},
            })
        pos = m.end()

    # Remaining plain text
    if pos < len(text):
        remaining = text[pos:]
        if remaining:
            segments.extend(_chunk_text(remaining, {}))

    return segments if segments else [{"type": "text", "text": {"content": text}}]


def _chunk_text(text: str, annotations: dict) -> list[dict]:
    """Split text into chunks of MAX_BLOCK_TEXT and return rich_text objects."""
    chunks = []
    for i in range(0, len(text), MAX_BLOCK_TEXT):
        obj: dict = {
            "type": "text",
            "text": {"content": text[i : i + MAX_BLOCK_TEXT]},
        }
        if annotations:
            obj["annotations"] = annotations
        chunks.append(obj)
    return chunks


def markdown_to_blocks(markdown: str) -> list[dict]:
    """Convert a markdown string to a list of Notion block objects."""
    lines = markdown.split("\n")
    blocks: list[dict] = []
    i = 0
    total = len(lines)

    while i < total:
        line = lines[i]
        stripped = line.strip()

        # Empty line → skip
        if not stripped:
            i += 1
            continue

        # Divider
        if stripped in ("---", "***", "___"):
            blocks.append({"type": "divider", "divider": {}})
            i += 1
            continue

        # Code block
        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            code_lines = []
            i += 1
            while i < total and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            if i < total:
                i += 1  # skip closing ```
            code_text = "\n".join(code_lines)
            if code_text:
                for chunk_start in range(0, len(code_text), MAX_BLOCK_TEXT):
                    chunk = code_text[chunk_start : chunk_start + MAX_BLOCK_TEXT]
                    blocks.append({
                        "type": "code",
                        "code": {
                            "rich_text": [{"type": "text", "text": {"content": chunk}}],
                            "language": lang or "plain text",
                        },
                    })
            continue

        # Table (markdown pipe table)
        if stripped.startswith("|"):
            table_rows = []
            while i < total and lines[i].strip().startswith("|"):
                row_text = lines[i].strip()
                i += 1  # always advance — prevents infinite loop
                # Skip separator rows like |---|---|
                if re.match(r"^\|[\s\-:|]+\|?$", row_text):
                    continue
                cells = [c.strip() for c in row_text.split("|")[1:-1]]
                if cells:
                    table_rows.append(cells)
            if table_rows:
                width = max(len(r) for r in table_rows)
                notion_rows = []
                for row in table_rows:
                    padded = row + [""] * (width - len(row))
                    notion_cells = [_parse_rich_text(cell) for cell in padded]
                    notion_rows.append({
                        "type": "table_row",
                        "table_row": {"cells": notion_cells},
                    })
                blocks.append({
                    "type": "table",
                    "table": {
                        "table_width": width,
                        "has_column_header": True,
                        "has_row_header": False,
                        "children": notion_rows,
                    },
                })
            continue

        # Headings
        if stripped.startswith("### "):
            blocks.append({
                "type": "heading_3",
                "heading_3": {"rich_text": _parse_rich_text(stripped[4:])},
            })
            i += 1
            continue
        if stripped.startswith("## "):
            blocks.append({
                "type": "heading_2",
                "heading_2": {"rich_text": _parse_rich_text(stripped[3:])},
            })
            i += 1
            continue
        if stripped.startswith("# "):
            blocks.append({
                "type": "heading_1",
                "heading_1": {"rich_text": _parse_rich_text(stripped[2:])},
            })
            i += 1
            continue

        # Blockquote
        if stripped.startswith("> "):
            quote_lines = []
            while i < total and lines[i].strip().startswith("> "):
                quote_lines.append(lines[i].strip()[2:])
                i += 1
            blocks.append({
                "type": "quote",
                "quote": {"rich_text": _parse_rich_text("\n".join(quote_lines))},
            })
            continue

        # Numbered list
        if re.match(r"^\d+\.\s", stripped):
            text = re.sub(r"^\d+\.\s", "", stripped)
            blocks.append({
                "type": "numbered_list_item",
                "numbered_list_item": {"rich_text": _parse_rich_text(text)},
            })
            i += 1
            continue

        # Bullet list
        if stripped.startswith("- ") or stripped.startswith("* "):
            blocks.append({
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": _parse_rich_text(stripped[2:])},
            })
            i += 1
            continue

        # Default: paragraph — collect contiguous non-special lines
        para_lines = []
        while i < total:
            l = lines[i].strip()
            if not l or l.startswith("#") or l.startswith("```") or l.startswith("|") or l.startswith("> ") or l.startswith("- ") or l.startswith("* ") or l in ("---", "***", "___") or re.match(r"^\d+\.\s", l):
                break
            para_lines.append(l)
            i += 1
        if para_lines:
            blocks.append({
                "type": "paragraph",
                "paragraph": {"rich_text": _parse_rich_text(" ".join(para_lines))},
            })
        else:
            # Safety: if nothing matched and nothing was consumed, skip the line
            i += 1

    return blocks
