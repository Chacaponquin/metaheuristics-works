import random
from domain import Data
from typing import Callable
from utils import insert_sorted


# P-HEURISTIC
class MhEvolutionStrategy:
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

        self.OBJECTIVE_MAX = False

    def run(
        self,
        generational: bool,
        generation_size: int,
        best_references: int,
        max_trials: int
    ) -> list[float]:
        print('Evolution Strategy')

        solutions = []
        for i in range(generation_size):
            solution: list[float] = self.random_solution(self.step)
            evaluation: float = self.objective_function(solution, self.data)
            solutions = insert_sorted(
                solutions,
                [evaluation, solution],
                best_references,
                self.OBJECTIVE_MAX
            )

        for g in range(0, int(max_trials / generation_size)):
            new_solutions = []

            for i in range(generation_size):
                parent = random.randint(0, best_references)

                # a change with respect to one of the best solutions
                solution = self.random_change(solutions[parent][1].copy(), self.step)
                evaluation = self.objective_function(solution, self.data)
                new_solutions = insert_sorted(
                    new_solutions,
                    [evaluation, solution],
                    best_references,
                    self.OBJECTIVE_MAX
                )

            if generational:
                solutions = new_solutions
            else:
                for i in range(best_references):
                    evaluation, solution = new_solutions[i][0], new_solutions[i][1]
                    solutions = insert_sorted(solutions, [evaluation, solution], best_references)

        best_solution = solutions[0][1]

        print(f'Best Solution: {best_solution}')

        return best_solution


# S-HEURISTIC
class MhHillClimb:
    def __init__(
            self,
            data: list[Data],
            step: float,
            random_change: Callable[[list[float], float], list[float]],
            random_solution: Callable[[float], list[float]],
            objective_function: Callable[[list[float], list[Data]], float]
    ):
        self.objective_function = objective_function
        self.data = data
        self.step = step

        self.random_change = random_change
        self.random_solution = random_solution

    def print(
            self,
            iteration: int,
            solution: list[float],
            error: float,
            best_error: float,
            best_solution: list[float]
    ):
        print(f"{iteration}: Solution: {solution}, Error: {error}, Best error: {best_error}, Best solution: {best_solution}")

    def run(self, max_trials: int) -> list[float]:
        print('Hill Climb')

        best_solution: list[float] = self.random_solution(self.step)
        best_evaluation = self.objective_function(best_solution, self.data)

        self.print(
            0,
            best_solution,
            best_evaluation,
            best_evaluation,
            best_solution
        )

        for i in range(max_trials):
            solution: list[float] = self.random_change(best_solution.copy(), self.step)
            evaluation: float = self.objective_function(solution, self.data)

            if abs(evaluation) < abs(best_evaluation):
                best_evaluation = evaluation
                best_solution = solution.copy()

            self.print(
                i + 1,
                solution,
                evaluation,
                best_evaluation,
                best_solution
            )

            if not bool(evaluation):
                break

        return best_solution
