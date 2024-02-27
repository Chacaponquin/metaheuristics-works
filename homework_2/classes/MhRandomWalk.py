from homework_2.core import random_solution, function, random_change
from homework_2.classes import Data


class MhRandomWalk:
    def __init__(self, data: list[Data], step: int):
        self.step = step
        self.data = data

    def run(self, iterations: int) -> list[float]:
        best_solution: list[float] = random_solution(step=self.step)
        best_evaluation: float = function(k_data=best_solution, data=self.data)

        last_solution = best_solution
        for i in range(1, iterations):
            solution: list[float] = random_change(ks=last_solution.copy(), step=self.step)
            evaluation = function(k_data=solution, data=self.data)
            last_solution = solution

            if abs(evaluation) < abs(best_evaluation):
                best_evaluation = evaluation
                best_solution = solution

        return best_solution
