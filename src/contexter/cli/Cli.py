import click
from .groups.template import createtask
from .groups._entry import init


@click.group(help="LLM Context and Memory Manager")
def cx():
    pass


cx.add_command(init)
cx.add_command(createtask)
