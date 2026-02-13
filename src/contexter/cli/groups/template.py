import click
from contexter.manager.workspace import WorkspaceManager
from typing import Optional
from datetime import datetime, timezone

manager = WorkspaceManager

utctime = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")


@click.group(help="create base template: default(claude)")
@click.option(
    "--task_name",
    default=utctime,
    required=False,
    help="- Name of the task. default(UTC timestamp)",
)
@click.option(
    "--provider",
    default="claude",
    required=False,
    help="- bypass default template",
    show_default=True,
)
def createtask(task_name: Optional[str], provider: Optional[str]):
    manager(task_name).task_setup()
