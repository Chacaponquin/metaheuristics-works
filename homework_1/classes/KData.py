import random


class KData:
    LIMIT_UP = 1
    LIMIT_DOWN = 0

    def __init__(self, step: float):
        self.step = step
        self.ks = self.generate_solution(self.step)

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

    def change_k_values(self, error: float):
        choice = random.randint(0, 4)
        if error < 0:
            self._down_k(choice)
        else:
            self._up_k(choice)

    def _up_k(self, index: int):
        if self.ks[index] < self.LIMIT_UP:
            self.ks[index] = self._round(self.ks[index] + self.step)

    def _down_k(self, index: int):
        if self.ks[index] > self.LIMIT_DOWN:
            self.ks[index] = self._round(self.ks[index] - self.step)

    @staticmethod
    def _round(value):
        return round(value, 1)

    @staticmethod
    def generate_solution(step: float):
        return [KData._gen_value(step) for _ in range(5)]

    @staticmethod
    def _gen_value(step: float) -> float:
        choices = []
        value = 0.0

        while value < KData.LIMIT_UP:
            choices.append(value)
            value = KData._round(value + step)

        return random.choice(choices)
