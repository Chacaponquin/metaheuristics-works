from homework_2.classes import Data
from rich.table import Table
from rich.console import Console
from typing import Callable
import pandas as pd


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

        self.columns = [
            "Iteration",
            "Solution",
            "Error",
            "Best Error",
            "Best Solution"
        ]

    def run(self, max_trials: int) -> list[float]:
        table = Table(title="Hill Climb")

        for col in self.columns:
            table.add_column(col)

        df = pd.DataFrame(columns=self.columns)

        best_solution: list[float] = self.random_solution(self.step)
        best_evaluation = self.objective_function(best_solution, self.data)

        # add row to table
        table.add_row(
            str(0),
            str(best_solution),
            str(best_evaluation),
            str(best_evaluation),
            str(best_solution)
        )

        # add row to csv
        df.loc['0'] = [
            str(0),
            str(best_solution),
            str(best_evaluation),
            str(best_evaluation),
            str(best_solution)
        ]

        for i in range(max_trials):
            solution: list[float] = self.random_change(best_solution.copy(), self.step)
            evaluation: float = self.objective_function(solution, self.data)

            if abs(evaluation) < abs(best_evaluation):
                best_evaluation = evaluation
                best_solution = solution.copy()

            # add row
            table.add_row(
                str(i + 1),
                str(solution),
                str(evaluation),
                str(best_evaluation),
                str(best_solution)
            )

            # add row to csv
            df.loc[str(i + 1)] = [
                str(i + 1),
                str(solution),
                str(evaluation),
                str(best_evaluation),
                str(best_solution)
            ]

            if not bool(evaluation):
                break

        console = Console()
        console.print(table)

        df.to_excel('../hill_climb.xlsx', index=False)

        return best_solution







