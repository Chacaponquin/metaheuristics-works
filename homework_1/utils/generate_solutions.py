import numpy as np
from itertools import product


def generate_solutions(step: float) -> list[list[float]]:
    return_data = []

    valors = np.arange(0, 1.1, step)
    combinations = list(product(valors, repeat=5))

    for comb in combinations:
        return_data.append([round(i, 1) for i in comb])

    return return_data

