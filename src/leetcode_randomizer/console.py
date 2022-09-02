import click

from . import __version__
from src.leetcode_randomizer import notion, utils

PATTERNS = utils.get_patterns()


@click.command(options_metavar="<options>")
@click.option(
    "--pattern",
    "-p",
    type=click.Choice(PATTERNS.keys()),
    default="linked",
    help="Select a pattern for the problems",
    metavar="<list[str]>",
)
@click.option(
    "--limit",
    "-l",
    default=5,
    help="Number of problems",
    show_default=True,
    metavar="<int>",
)
@click.version_option(version=__version__)
def main(limit, pattern):
    """The Leetcode Randomizer CLI Project.

    Get a random set of problems you have already solved for a particular pattern.

    \b
    Choose a pattern from the following:
    1. arr  :   Array
    2. dict :   Hash Table
    \f

    Args:
        limit (int): Number of problems to solve
        pattern (str): Pattern Type
    """
    click.echo(f"Limit: {limit} Pattern: {PATTERNS[pattern]}")
    final_problems = randomize()

    for prob in final_problems:
        click.echo(f"No.: {prob.prob_id}   Problem: {prob.name}")


def randomize(limit: int = 5):
    problems = notion.get_all_records()
    prob_ids = list(problems.keys())
    prob_set = set()

    while len(prob_set) < limit:
        number = utils.get_random_prob(prob_ids)
        prob_set.add(number)

    random_prob_list = [problems[prob_id] for prob_id in prob_set]
    return random_prob_list
