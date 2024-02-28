from homework_2.core import random_solution, function, random_change
from homework_2.classes import Data
from rich.table import Table
from rich.console import Console


class MhHillClimb:
    def __init__(self, data: list[Data], step: float):
        self.data = data
        self.step = step

    def run(self, max_trials: int) -> list[float]:
        table = Table(title="Hill Climb")

        table.add_column("Iteration")
        table.add_column("Solution")
        table.add_column("Error")
        table.add_column("Best Error")
        table.add_column('Best Solution')

        best_solution: list[float] = random_solution(step=self.step)
        best_evaluation = function(k_data=best_solution, data=self.data)

        # add row
        table.add_row(str(0), str(best_solution), str(best_evaluation), str(best_evaluation), str(best_solution))

        for i in range(max_trials):
            solution: list[float] = random_change(ks=best_solution.copy(), step=self.step)
            evaluation: float = function(k_data=solution, data=self.data)

            if abs(evaluation) < abs(best_evaluation):
                best_evaluation = evaluation
                best_solution = solution.copy()

            # add row
            table.add_row(str(i + 1), str(solution), str(evaluation), str(best_evaluation), str(best_solution))

            if not bool(evaluation):
                break

        console = Console()
        console.print(table)

        return best_solution







