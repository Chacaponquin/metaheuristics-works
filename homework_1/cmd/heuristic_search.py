from rich.console import Console
from rich.table import Table
from homework_1.classes import Data, KData
from homework_1.utils import read_data, function


def heuristic_search(data: list[Data], iterations: int, step: float, log: bool):
    table = Table(title="Heuristic search", padding=1)

    table.add_column('Iteration')
    table.add_column("Test-K")
    table.add_column("Error")
    table.add_column("Best Error")
    table.add_column('Best Solution')

    best_error = None
    best_solution = None

    ks = KData(step=step)
    for it in range(iterations):
        error = function(ks.ks, data)

        if best_error is not None:
            if abs(error) < abs(best_error):
                best_error = error
                best_solution = ks.ks.copy()
        else:
            best_error = error
            best_solution = ks.ks.copy()

        # change k values
        ks.change_k_values(error)

        table.add_row(str(it + 1), str(ks.ks.copy()), str(error), str(best_error), str(best_solution))

    if log:
        console = Console()
        console.print(table)

    return best_solution, best_error


if __name__ == '__main__':
    data = read_data()
    heuristic_search(data=data, iterations=100, step=0.1, log=True)