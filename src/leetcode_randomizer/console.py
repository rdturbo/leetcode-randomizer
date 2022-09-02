import click


from . import __version__
from src.leetcode_randomizer import notion, utils
from src.leetcode_randomizer.problem import Problem

PATTERNS = utils.get_patterns()


@click.command(options_metavar="<options>")
@click.option(
    "--pattern",
    "-p",
    type=click.Choice(PATTERNS.keys()),
    default="linked",
    help="Select a pattern for the problems",
    metavar="<list[pattern]>",
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
    01. array       : Array
    02. binary      : Binary Search
    03. bit         : Bit Manipulation
    04. dict        : Hash Table
    05. dp          : DP
    06. graph       : Graph
    07. greedy      : Greedy
    08. heap        : Heap
    09. interval    : Intervals
    10. linked      : Linked List
    11. math        : Math
    12. matrix      : Matrix
    13. prefix      : PrefixSums
    14. queue       : Queue
    15. recursion   : Recursion
    16. sliding     : Sliding Window
    17. stack       : Stack
    18. string      : String
    19. tree        : Tree
    20. two         : Two Pointers
    \f

    Args:
        limit (int): Number of problems to solve
        pattern (str): Pattern Type
    """
    selected_pattern = PATTERNS[pattern]
    click.echo(f"Limit: {limit} Pattern: {selected_pattern}")

    final_problems = randomize(limit, selected_pattern)

    for prob in final_problems:
        diff = prob.diffculty
        print_str = f"No.: {utils.get_num_padding(prob.prob_id)}\tProblem: {prob.name}"
        if diff == "Easy":
            click.secho(print_str, fg="green")
        elif diff == "Medium":
            click.secho(print_str, fg="yellow")
        else:
            click.secho(print_str, fg="red")


def randomize(limit: int, pattern: str) -> list[Problem]:
    """Returns list of <limit> problems of <pattern> type."""
    problems = notion.get_all_records(pattern)
    prob_ids = list(problems.keys())
    prob_set = set()

    while len(prob_set) < limit:
        number = utils.get_random_prob(prob_ids)
        prob_set.add(number)

    random_prob_list = [problems[prob_id] for prob_id in prob_set]
    return random_prob_list
