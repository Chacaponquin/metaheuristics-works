import random
from domain import KData, Data
from typing import Callable


class Heuristic:
    def __init__(
        self,
        step: float,
        objective_function: Callable[[list[float], list[Data]], float],
        random_solution: Callable[[float], list[float]],
        data: list[Data],
    ):
        self.step = step
        self.random_solution = random_solution
        self.objective_function = objective_function
        self.data = data

    def run(self, iterations: int):
        best_error = None
        best_solution = None

        ks = self.random_solution(self.step)
        for it in range(iterations):
            error = self.objective_function(ks, self.data)

            if best_error is not None:
                if abs(error) < abs(best_error):
                    best_error = error
                    best_solution = ks.copy()
            else:
                best_error = error
                best_solution = ks.copy()

            if not bool(error):
                break

            # change k values
            self.change_k_values(ks, error)

        print(f'Best Solution: {best_solution}, Best Error: {best_error}')

        return best_solution

    def change_k_values(self, ks: list[float], error: float):
        choice = random.randint(0, 4)
        if error < 0:
            self.down_k(ks, choice)
        else:
            self.up_k(ks, choice)

    def up_k(self, ks: list[float], index: int):
        if ks[index] < KData.LIMIT_UP:
            ks[index] = KData.round(ks[index] + self.step)

    def down_k(self, ks: list[float], index: int):
        if ks[index] > KData.LIMIT_DOWN:
            ks[index] = round(ks[index] - self.step)


