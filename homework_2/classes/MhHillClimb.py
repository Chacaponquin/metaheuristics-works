from homework_2.core import random_solution, function, random_change
from homework_2.classes import Data


class MhHillClimb:
    def __init__(self, data: list[Data], step: float):
        self.data = data
        self.step = step

    def run(self, iterations: int) -> list[float]:
        best_solution: list[float] = random_solution(step=self.step)
        best_evaluation = function(k_data=best_solution, data=self.data)

        for i in range(iterations):
            solution = random_change(ks=best_solution.copy(), step=self.step)
            evaluation = function(k_data=solution, data=self.data)

            if abs(evaluation) < abs(best_evaluation):
                best_evaluation = evaluation
                best_solution = solution

        return best_solution







