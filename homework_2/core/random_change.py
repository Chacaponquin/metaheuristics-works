import random
from homework_2.classes import KData


def random_change(ks: list[float], step: float) -> list[float]:
    index_choice = random.randint(0, 4)
    up_choice = random.randint(0, 1)

    if up_choice == 0:
        up_k(ks=ks, index=index_choice, step=step)
    else:
        down_k(ks=ks, index=index_choice, step=step)

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
