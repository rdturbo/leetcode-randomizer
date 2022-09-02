import random
from src.leetcode_randomizer.problem import Problem


def dict_decoder(x: dict | list) -> list[str]:
    """Returns list of keys in dictionary"""
    return [i for i in x]


def get_problem_map(pagination_list: list) -> dict[int, Problem]:
    """Returns dictionary of problem objects mapped from problem id"""
    problem_map = {}
    for records in pagination_list:
        for record in records["results"]:
            problem = Problem.decode_data(record)
            problem_map[problem.prob_id] = problem

    return problem_map


def get_random_prob(problem_numbers: list[int]) -> int:
    return random.choice(problem_numbers)


def get_num_padding(num: int) -> str:
    return "{:4d}".format(num)


def get_patterns():
    return {
        "array": "Array",
        "binary": "Binary Search",
        "bit": "Bit Manipulation",
        "dict": "Hash Table",
        "dp": "DP",
        "graph": "Graph",
        "greedy": "Greedy",
        "heap": "Heap",
        "interval": "Intervals",
        "linked": "Linked List",
        "math": "Math",
        "matrix": "Matrix",
        "prefix": "PrefixSums",
        "queue": "Queue",
        "recursion": "Recursion",
        "sliding": "Sliding Window",
        "stack": "Stack",
        "tree": "Tree",
        "two": "Two Pointers",
    }
