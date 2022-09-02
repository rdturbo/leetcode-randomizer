from problem import Problem


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
