import random
from domain import KData


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