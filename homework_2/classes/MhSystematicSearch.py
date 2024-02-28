from homework_2.classes import Data, KData
from homework_2.core import random_solution, function, not_random_solution, not_random_change
from rich.table import Table
from rich.console import Console


class MhSystematicSearch:
    def __init__(self, data: list[Data], step: float):
        self.step = step
        self.data = data

        self.OBJECTIVE_MAX = False

    def run(self, max_trials: int, systematic_s_ini: bool):
        table = Table(title="Systematic Search")

        table.add_column("Iteration")
        table.add_column("Solution")
        table.add_column("Error")
        table.add_column("Best Error")
        table.add_column('Best Solution')

        if systematic_s_ini:
            best_solution = not_random_solution(min_value=KData.LIMIT_DOWN)
        else:
            best_solution = random_solution(step=self.step)
        best_evaluation = function(k_data=best_solution, data=self.data)

        # add row
        table.add_row(
            str(0),
            str(best_solution),
            str(best_evaluation),
            str(best_evaluation),
            str(best_solution)
        )

        solution = best_solution.copy()
        for i in range(1, max_trials):
            solution: list[float] = not_random_change(
                solution=solution,
                step=self.step,
                max_value=KData.LIMIT_UP,
                min_value=KData.LIMIT_DOWN
            )

            evaluation: float = function(k_data=solution, data=self.data)

            if self.is_better_than(evaluation, best_evaluation):
                best_evaluation = evaluation
                best_solution = solution.copy()

            # add row
            table.add_row(str(i + 1), str(solution), str(evaluation), str(best_evaluation), str(best_solution))

            if not bool(evaluation):
                break

        console = Console()
        console.print(table)

        return best_solution

    def is_better_than(self, evaluation1: float, evaluation2: float):
        greater1 = abs(evaluation1) > abs(evaluation2)
        return (((evaluation1 == evaluation2)) or (self.OBJECTIVE_MAX) and greater1) or (not (self.OBJECTIVE_MAX) and not greater1)
