import random


def random_combination(solution: list[float], solution_alt: list[float]):
    length = len(solution)
    for i in range(len(solution)):
        if random.randint(0, length):
            solution[i] = solution_alt[i]

    return solution
