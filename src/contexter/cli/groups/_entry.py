import click
from contexter.manager.workspace import WorkspaceManager
from typing import Optional
from datetime import datetime, timezone
from contexter.manager.config import initialize_project

manager = WorkspaceManager

utctime = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")


@click.command(help="setup prompt templates")
@click.option("--provider", default="claude", help="- create base template")
def init(provider: Optional[str]):
    initialize_project(provider)
