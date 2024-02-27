import random
from homework_1.utils.generate_solution import generate_solution


class KData:
    LIMIT_UP = 1
    LIMIT_DOWN = 0

    STEP_DEFAULT = 0.1

    def __init__(self, step: float):
        self.step = step
        self.ks = generate_solution(self.step)

    @property
    def k1(self):
        return self.ks[0]

    @property
    def k2(self):
        return self.ks[1]

    @property
    def k3(self):
        return self.ks[2]

    @property
    def k4(self):
        return self.ks[3]

    @property
    def k5(self):
        return self.ks[4]


    @staticmethod
    def round(value):
        return round(value, 1)


