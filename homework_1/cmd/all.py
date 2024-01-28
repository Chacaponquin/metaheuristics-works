from rich.console import Console
from rich.table import Table
from homework_1.cmd import random_search, heuristic_search, exhaustive_search
from homework_1.utils import read_data


def main():
    data = read_data()
    iterations = 100
    step = 0.1

    best_random_solution, best_random_error = random_search(data=data, iterations=iterations, step=step, log=False)
    best_heuristic_solution, best_heuristic_error = heuristic_search(data=data, iterations=iterations, step=step, log=False)
    best_exhaustive_solution, best_exhaustive_error = exhaustive_search(data=data, step=step, log=False)

    table = Table(title="All searches", padding=1)

    table.add_column("Search")
    table.add_column("Best solution")
    table.add_column('Error')

    table.add_row("Random search", str(best_random_solution), str(best_random_error))
    table.add_row("Heuristic search", str(best_heuristic_solution), str(best_heuristic_error))
    table.add_row("Exhaustive search", str(best_exhaustive_solution), str(best_exhaustive_error))

    console = Console()
    console.print(table)


if __name__ == '__main__':
    main()
