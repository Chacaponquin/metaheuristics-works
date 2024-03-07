from domain import Data
from operators import random_list, min_value_list, next_list, add_or_minus_one_param, random_crossing


def objective_function(k_data: list[float], data: list[Data]):
    error = 0
    k1, k2, k3, k4, k5 = k_data

    for i in range(len(data)):
        if i != 0:
            p = (k1 * data[i - 1].data[0] +
                 k2 * data[i - 1].data[1] +
                 k3 * data[i - 1].data[2] +
                 k4 * data[i - 1].data[3] +
                 k5 * data[i - 1].data[4])

            error += data[i].data[5] - p

    return round(error, 4)


def random_solution(step: float):
    return random_list(step=step)


def not_random_solution(min_value: float):
    return min_value_list(min_value=min_value)


def random_change(solution: list[float], step: float):
    return add_or_minus_one_param(ks=solution, step=step)


def not_random_change(solution: list[float], min_value: float, max_value: float, step: float):
    return next_list(solution=solution, step=step, min_value=min_value, max_value=max_value)


def random_combination(solution: list[float], solution_alt: list[float]):
    return random_crossing(solution=solution, solution_alt=solution_alt)