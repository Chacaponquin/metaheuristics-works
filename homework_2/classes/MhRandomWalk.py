from homework_2.classes import Data
from typing import Callable


class MhRandomWalk:
    def __init__(
            self,
            data: list[Data],
            step: float,
            random_change: Callable[[list[float], float], list[float]],
            random_solution: Callable[[float], list[float]],
            objective_function: Callable[[list[float], list[Data]], float]
    ):
        self.objective_function = objective_function
        self.step = step
        self.data = data
        self.random_change = random_change
        self.random_solution = random_solution

    def run(self, iterations: int) -> list[float]:
        best_solution: list[float] = self.random_solution(self.step)
        best_evaluation: float = self.objective_function(best_solution, self.data)

        last_solution = best_solution
        for i in range(1, iterations):
            solution: list[float] = self.random_change(last_solution.copy(), self.step)
            evaluation: float = self.objective_function(solution, self.data)
            last_solution = solution

            if abs(evaluation) < abs(best_evaluation):
                best_evaluation = evaluation
                best_solution = solution

        return best_solution
