import click

from . import __version__
from src.leetcode_randomizer import notion


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""
    click.echo("Hello, world!")
    problems = notion.get_all_records()
    click.echo(problems[83])
