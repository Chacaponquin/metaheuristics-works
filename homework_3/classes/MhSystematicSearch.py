from homework_2.classes import Data, KData
from homework_2.utils import is_better_than
from rich.table import Table
from rich.console import Console
from typing import Callable


class MhSystematicSearch:
    def __init__(
            self,
            data: list[Data],
            step: float,
            random_solution: Callable[[float], list[float]],
            not_random_change: Callable[[list[float], float, float, float], list[float]],
            not_random_solution: Callable[[float], list[float]],
            objective_function: Callable[[list[float], list[Data]], float]
    ):
        self.objective_function = objective_function
        self.step = step
        self.data = data
        self.random_solution = random_solution
        self.not_random_change = not_random_change
        self.not_random_solution = not_random_solution

        self.OBJECTIVE_MAX = False

    def run(self, max_trials: int, systematic_s_ini: bool):
        table = Table(title="Systematic Search")

        table.add_column("Iteration")
        table.add_column("Solution")
        table.add_column("Error")
        table.add_column("Best Error")
        table.add_column('Best Solution')

        if systematic_s_ini:
            best_solution = self.not_random_solution(KData.LIMIT_DOWN)
        else:
            best_solution = self.random_solution(self.step)
        best_evaluation = self.objective_function(best_solution, self.data)

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
            solution: list[float] = self.not_random_change(
                solution,
                KData.LIMIT_UP,
                KData.LIMIT_DOWN,
                self.step
            )

            evaluation: float = self.objective_function(solution, self.data)

            if is_better_than(evaluation, best_evaluation, self.OBJECTIVE_MAX):
                best_evaluation = evaluation
                best_solution = solution.copy()

            # add row
            table.add_row(
                str(i + 1),
                str(solution),
                str(evaluation),
                str(best_evaluation),
                str(best_solution))

            if not bool(evaluation):
                break

        console = Console()
        console.print(table)

        return best_solution

