"""CLI entrypoint for FrontierWatch."""

from __future__ import annotations

import logging
import sys
from datetime import date

import click
from dotenv import load_dotenv

load_dotenv()


@click.group()
@click.option("-v", "--verbose", is_flag=True, help="Enable debug logging.")
def main(verbose: bool) -> None:
    """FrontierWatch — Automated area briefing pipeline."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stderr,
    )


@main.command()
@click.argument(
    "briefing",
    type=click.Choice(
        ["biotech", "computing-ai", "economics", "energy", "monetary-policy", "securities-futures"],
        case_sensitive=False,
    ),
)
@click.option("--date", "end_date", type=click.DateTime(formats=["%Y-%m-%d"]), default=None, help="End date for coverage window (default: today).")
def run(briefing: str, end_date: date | None) -> None:
    """Run a single area briefing pipeline."""
    from frontierwatch.briefings import BRIEFINGS

    end = end_date.date() if end_date else None
    cls = BRIEFINGS[briefing]
    instance = cls()

    click.echo(f"Running {instance.name}...")
    url = instance.run(end_date=end)
    click.echo(f"Published: {url}")


@main.command(name="run-all")
@click.option("--date", "end_date", type=click.DateTime(formats=["%Y-%m-%d"]), default=None, help="End date for coverage window (default: today).")
def run_all(end_date: date | None) -> None:
    """Run all area briefings."""
    from frontierwatch.briefings import BRIEFINGS

    end = end_date.date() if end_date else None
    for name, cls in BRIEFINGS.items():
        instance = cls()
        click.echo(f"Running {instance.name}...")
        try:
            url = instance.run(end_date=end)
            click.echo(f"  Published: {url}")
        except Exception as e:
            click.echo(f"  FAILED: {e}", err=True)


@main.command()
def list_briefings() -> None:
    """List all available briefings."""
    from frontierwatch.briefings import BRIEFINGS

    for slug, cls in BRIEFINGS.items():
        instance = cls()
        click.echo(f"  {slug:25s} {instance.name}")


if __name__ == "__main__":
    main()
