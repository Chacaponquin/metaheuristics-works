from homework_2.classes import Data
from homework_2.core import function, random_solution


class MhRandomSearch:
    def __init__(self, data: list[Data], step: int):
        self.step = step
        self.data = data

    def run(self, iterations: int) -> list[float]:
        best_solution: list[float] = random_solution(step=self.step)
        best_evaluation: float = function(k_data=best_solution, data=self.data)

        for i in range(1, iterations):
            solution = random_solution(step=self.step)
            evaluation = function(k_data=solution, data=self.data)

            if abs(evaluation) < abs(best_evaluation):
                best_evaluation = evaluation
                best_solution = solution

        return best_solution
