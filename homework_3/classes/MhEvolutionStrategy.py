import random
from homework_2.classes import Data
from homework_2.utils import insert_sorted
from rich.table import Table
from rich.console import Console
from typing import Callable
import pandas as pd


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

        self.columns = [
            "Generation",
            "Solutions",
            "New Solutions",
            "Solutions"
        ]

    def run(
            self,
            generational: bool,
            generation_size: int,
            best_references: int,
            max_trials: int
    ) -> list[float]:
        table = Table(title="Genetic Algorithm")

        df = pd.DataFrame(columns=self.columns)

        for col in self.columns:
            table.add_column(col)

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

            # add row to table
            table.add_row(
                str(g + 1),
                str(solutions),
                str(new_solutions),
                str(solutions)
            )

            # add row to csv
            df.loc[str(g + 1)] = [
                str(g + 1),
                str(solutions),
                str(new_solutions),
                str(solutions)
            ]

        best_solution = solutions[0][1]

        console = Console()
        console.print(table)

        df.to_excel('../evolution_strategy.xlsx', index=False)

        print(f'Best Solution: {best_solution}')

        return best_solution




