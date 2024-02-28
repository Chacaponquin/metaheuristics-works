from homework_2.classes import Data
from homework_2.core import function, random_solution
from rich.table import Table
from rich.console import Console


class MhRandomSearch:
    def __init__(self, data: list[Data], step: float):
        self.step = step
        self.data = data

    def run(self, iterations: int) -> list[float]:
        table = Table(title="Random Search")

        table.add_column("Iteration")
        table.add_column("Solution")
        table.add_column("Error")
        table.add_column("Best Error")
        table.add_column('Best Solution')

        best_solution: list[float] = random_solution(step=self.step)
        best_evaluation: float = function(k_data=best_solution, data=self.data)

        # add row
        table.add_row(
            str(0),
            str(best_solution),
            str(best_evaluation),
            str(best_evaluation),
            str(best_solution)
        )

        for i in range(1, iterations):
            solution = random_solution(step=self.step)
            evaluation = function(k_data=solution, data=self.data)

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
