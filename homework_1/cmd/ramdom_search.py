from rich.console import Console
from rich.table import Table
from homework_1.classes import Data, KData
from homework_1.utils import read_data, function


def random_search(data: list[Data], iterations: int, step: float, log: bool):
    table = Table(title="Random search", padding=1)

    table.add_column('Iteration')
    table.add_column("Test-K")
    table.add_column("Error")
    table.add_column("Best Error")
    table.add_column('Best Solution')

    best_error = None
    best_solution = None

    for index in range(iterations):
        ks = KData(step=step)
        error = abs(function(ks.ks, data))

        if best_error is not None:
            if error < best_error:
                best_error = error
                best_solution = ks.ks.copy()
        else:
            best_error = error
            best_solution = ks.ks.copy()

        table.add_row(str(index), str(ks.ks.copy()), str(error), str(best_error), str(best_solution))

    if log:
        console = Console()
        console.print(table)

    return best_solution, best_error


if __name__ == '__main__':
    data = read_data()
    random_search(data=data, iterations=100, step=0.1, log=True)


