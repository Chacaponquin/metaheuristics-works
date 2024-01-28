from rich.console import Console
from rich.table import Table
from homework_1.classes import Data
from homework_1.utils import read_data, function, generate_solutions


def exhaustive_search(step: float, data: list[Data], log: bool):
    table = Table(title="Exhaustive search")

    table.add_column("Test-K")
    table.add_column("Error")
    table.add_column("Best Error")
    table.add_column('Best Solution')

    best_error = None
    best_solution = None
    worst_error = None
    worst_solution = None

    all_solutions = generate_solutions(step=step)

    for solution in all_solutions:
        error = abs(function(solution, data))

        if best_error is not None and worst_error is not None:
            if error < best_error:
                best_error = error
                best_solution = solution.copy()

            if error > worst_error:
                worst_error = error
                worst_solution = solution.copy()
        else:
            best_error = error
            worst_error = error
            worst_solution = solution.copy()
            best_solution = solution.copy()

        table.add_row(str(solution.copy()), str(error), str(best_error), str(best_solution))

    result_table = Table(title="Resultados")
    result_table.add_row("Mejor solución", str(best_solution))
    result_table.add_row("Peor solución", str(worst_solution))
    result_table.add_row("Mejor error", str(best_error))
    result_table.add_row("Peor error", str(worst_error))

    if log:
        console = Console()
        console.print(table)
        console.print(result_table)

    return best_solution, best_error


if __name__ == '__main__':
    data = read_data()
    exhaustive_search(data=data, step=0.1, log=True)
