import random
from homework_2.classes import KData, Data


## MUTATION

# añadir o restar el paso a uno de los 5 parámetros de forma aleatoria (random)
def add_or_minus_one_param(ks: list[float], step: float) -> list[float]:
    index_choice = random.randint(0, 4)
    up_choice = random.randint(0, 1)

    if up_choice == 0:
        up_k(ks=ks, index=index_choice, step=step)
    else:
        down_k(ks=ks, index=index_choice, step=step)

    return ks.copy()


# añadir el paso a uno de los 5 parámetros y restar el paso a otro de los parámetros (random)
def add_one_minus_one(ks: list[float], step: float) -> list[float]:
    first_index_choice = random.randint(0, 4)
    second_index_choice = random.randint(0, 4)

    while first_index_choice == second_index_choice:
        second_index_choice = random.randint(0, 4)

    up_k(ks=ks, index=first_index_choice, step=step)
    down_k(ks=ks, index=second_index_choice, step=step)

    return ks.copy()


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


def up_k(ks: list[float], index: int, step: float):
    if ks[index] < KData.LIMIT_UP:
        ks[index] = KData.round(ks[index] + step)
    else:
        ks[index] = KData.LIMIT_DOWN


def down_k(ks: list[float], index: int, step: float):
    if ks[index] > KData.LIMIT_DOWN:
        ks[index] = KData.round(ks[index] - step)
    else:
        ks[index] = KData.LIMIT_UP


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


## OBJECTIVE FUNCTION
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
