import random
from homework_2.classes import Data
from homework_2.core import random_solution, function, random_change
from homework_2.utils import insert_sorted
from rich.table import Table
from rich.console import Console


class MhEvolutionStrategy:
    def __init__(self, data: list[Data], step: float):
        self.step = step
        self.data = data

        self.OBJECTIVE_MAX = False

    def run(self, generational: bool, generation_size: int, best_references: int, max_trials: int) -> list[float]:
        table = Table(title="Genetic Algorithm")

        table.add_column("Generation")
        table.add_column("Solutions")
        table.add_column("New Solutions")
        table.add_column("Solutions")

        solutions = []
        for i in range(generation_size):
            solution: list[float] = random_solution(step=self.step)
            evaluation: float = function(k_data=solution, data=self.data)
            solutions = insert_sorted(
                solutions,
                [evaluation, solution],
                best_references,
                self.OBJECTIVE_MAX
            )

        for g in range(1, int(max_trials / generation_size)):
            new_solutions = []

            for i in range(generation_size):
                parent = random.randint(0, best_references)

                # a change with respect to one of the best solutions
                solution = random_change(ks=solutions[parent][1].copy(), step=self.step)
                evaluation = function(k_data=solution, data=self.data)
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




