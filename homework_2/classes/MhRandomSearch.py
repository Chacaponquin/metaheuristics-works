from homework_2.classes import Data
from rich.table import Table
from rich.console import Console
from typing import Callable


class MhRandomSearch:
    def __init__(
            self,
            data: list[Data],
            step: float,
            random_solution: Callable[[float], list[float]],
            objective_function: Callable[[list[float], list[Data]], float]
    ):
        self.objective_function = objective_function
        self.step = step
        self.data = data
        self.random_solution = random_solution

    def run(self, iterations: int) -> list[float]:
        table = Table(title="Random Search")

        table.add_column("Iteration")
        table.add_column("Solution")
        table.add_column("Error")
        table.add_column("Best Error")
        table.add_column('Best Solution')

        best_solution: list[float] = self.random_solution(self.step)
        best_evaluation: float = self.objective_function(best_solution, self.data)

        # add row
        table.add_row(
            str(0),
            str(best_solution),
            str(best_evaluation),
            str(best_evaluation),
            str(best_solution)
        )

        for i in range(1, iterations):
            solution: list[float] = self.random_solution(self.step)
            evaluation: float = self.objective_function(solution, self.data)

            if abs(evaluation) < abs(best_evaluation):
                best_evaluation = evaluation
                best_solution = solution

            # add row
            table.add_row(
                str(i + 1),
                str(best_solution),
                str(best_evaluation),
                str(best_evaluation),
                str(best_solution)
            )

            if not bool(evaluation):
                break

        console = Console()
        console.print(table)

        return best_solution
