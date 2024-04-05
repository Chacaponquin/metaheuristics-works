import random
from homework_2.classes import Data
from homework_2.utils import insert_sorted
from rich.table import Table
from rich.console import Console
from typing import Callable


class MhGeneticAlgorithm:
    def __init__(
            self,
            data: list[Data],
            step: float,
            random_solution: Callable[[float], list[float]],
            random_combination: Callable[[list[float], list[float]], list[float]],
            objective_function: Callable[[list[float], list[Data]], float]
    ):
        self.objective_function = objective_function
        self.step = step
        self.data = data
        self.random_solution = random_solution
        self.random_combination = random_combination

        self.OBJECTIVE_MAX = False  # goal of the optimization, True: maximization, False: minimization

    def run(self, max_trials: int, generational: bool, generation_size: int, best_references: int):
        table = Table(title="Genetic Algorithm")

        table.add_column("Generation")
        table.add_column("Solutions")
        table.add_column("New Solutions")
        table.add_column("Solutions")

        solutions = []

        for i in range(generation_size):
            solution = self.random_solution(self.step)
            evaluation = self.objective_function(solution, self.data)
            solutions = insert_sorted(
                solutions,
                [evaluation, solution],
                best_references,
                self.OBJECTIVE_MAX
            )

        for g in range(1, int(max_trials / generation_size)):
            new_solutions = []

            for i in range(generation_size):
                parent1 = random.randint(0, best_references)
                parent2 = random.randint(0, best_references)

                # a combination of two of the best solutions
                solution = self.random_combination(solutions[parent1][1].copy(), solutions[parent2][1].copy())
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
                        solutions,
                        [evaluation, solution],
                        best_references,
                        self.OBJECTIVE_MAX
                    )

            table.add_row(
                str(g + 1),
                str(solutions),
                str(new_solutions),
                str(solutions)
            )

        best_solution = solutions[0][1]

        console = Console()
        console.print(table)

        print(f'Best Solution: {best_solution}')

        return best_solution




