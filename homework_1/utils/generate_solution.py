import random
from homework_1.classes import KData


def generate_solution(step: float):
    return [gen_value(step) for _ in range(5)]


def gen_value(step: float) -> float:
    choices = []
    value = 0.0

    while value < KData.LIMIT_UP:
        choices.append(value)
        value = KData.round(value + step)

    return random.choice(choices)
