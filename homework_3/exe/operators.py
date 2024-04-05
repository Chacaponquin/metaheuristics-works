import random
from domain import KData


# next list (not random)
def next_list(
    solution: list[float],
    max_value: float,
    min_value: float,
    step: float
) -> list[float]:
    j = 4
    while (solution[j] == max_value) and j >= 0:
        j -= 1

    if j == -1:
        solution = min_value_list(min_value=min_value)
    else:
        solution[j] += step
        if solution[j] > max_value:
            solution[j] = max_value
        for j in range(j + 1, 5):
            solution[j] = min_value

    return solution.copy()


## SOLUTION
# crea una lista con valores aleatorios (random)
def random_list(step: float) -> list[float]:
    return [gen_value(step) for _ in range(5)]


# crea una lista con el menor valor indicado (not random)
def min_value_list(min_value: float):
    solution = [min_value for _ in range(5)]
    return solution


def gen_value(step: float) -> float:
    choices = []
    value = 0.0

    while value < KData.LIMIT_UP:
        choices.append(value)
        value = KData.round(value + step)

    return random.choice(choices)


## COMBINATION

# cruzamiento aleatorio
def random_crossing(solution: list[float], solution_alt: list[float]):
    length = len(solution)
    for i in range(len(solution)):
        if random.randint(0, length):
            solution[i] = solution_alt[i]

    return solution.copy()
