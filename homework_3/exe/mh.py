import random
from domain import Data
from typing import Callable
from utils import insert_sorted


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

            if not bool(evaluation):
                break

        print(f'Best solution: {best_solution}, Best Error: {best_evaluation}')

        return best_solution


# RANDOM SEARCH
class MhRandomSearch:
    def __init__(
            self,
            data: list[Data],
            step: float,
            random_solution: Callable[[float], list[float]],
            objective_function: Callable[[list[float], list[Data]], float],
            max_trials: int
    ):
        self.objective_function = objective_function
        self.step = step
        self.data = data
        self.random_solution = random_solution
        self.max_trials = max_trials

    def run(self) -> list[float]:
        best_solution: list[float] = self.random_solution(self.step)
        best_evaluation: float = self.objective_function(best_solution, self.data)

        for i in range(1, self.max_trials):
            solution: list[float] = self.random_solution(self.step)
            evaluation: float = self.objective_function(solution, self.data)

            if abs(evaluation) < abs(best_evaluation):
                best_evaluation = evaluation
                best_solution = solution

            if not bool(evaluation):
                break

        print(f'Best solution: {best_solution}, Best Error: {best_evaluation}')

        return best_solution


# P-HEURISTIC
class MhEvolutionStrategy:
    def __init__(
        self,
        data: list[Data],
        step: float,
        random_change: Callable[[list[float], float], list[float]],
        random_solution: Callable[[float], list[float]],
        objective_function: Callable[[list[float], list[Data]], float],
        max_trials: int
    ):
        self.objective_function = objective_function
        self.step = step
        self.data = data
        self.random_change = random_change
        self.random_solution = random_solution
        self.max_trials = max_trials

        self.OBJECTIVE_MAX = False

    def run(
        self,
        generational: bool,
        generation_size: int,
        best_references: int,
    ) -> list[float]:
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

        for g in range(0, int(self.max_trials / generation_size)):
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
                    solutions = insert_sorted(
                        list=solutions,
                        element=[evaluation, solution],
                        first_n=best_references,
                        objective_max=self.OBJECTIVE_MAX
                    )

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
        objective_function: Callable[[list[float], list[Data]], float],
        max_trials: int,
    ):
        self.objective_function = objective_function
        self.data = data
        self.step = step

        self.random_change = random_change
        self.random_solution = random_solution

        self.max_trials = max_trials

    def run(self) -> list[float]:
        best_solution: list[float] = self.random_solution(self.step)
        best_evaluation = self.objective_function(best_solution, self.data)

        for i in range(self.max_trials):
            solution: list[float] = self.random_change(best_solution.copy(), self.step)
            evaluation: float = self.objective_function(solution, self.data)

            if abs(evaluation) < abs(best_evaluation):
                best_evaluation = evaluation
                best_solution = solution.copy()

            if not bool(evaluation):
                break

        print(f'Best solution: {best_solution}, Best Error: {best_evaluation}')

        return best_solution
