import random


def random_combination(solution: list[float], solution_alt: list[float]):
    l = len(solution)
    for i in range(0, len(solution)):
        if random.randint(0, l):
            solution[i] = solution_alt[i]

    return solution
