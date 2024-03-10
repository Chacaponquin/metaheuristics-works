from mh import MhHillClimb, MhEvolutionStrategy, MhRandomSearch
from problemMilitaryBudget import random_change, random_solution, objective_function
from utils import read_data
from domain import Data


def main():
    data: list[Data] = read_data()
    max_trials = 1000
    step = 0.1

    # ejecutar escalador de colina
    hill_climb = MhHillClimb(
        step=step,
        data=data,
        random_change=random_change,
        random_solution=random_solution,
        objective_function=objective_function,
        max_trials=max_trials
    )

    hill_climb.run()

    print()

    # ejecutar evolution strategy
    evolution_strategy = MhEvolutionStrategy(
        data=data,
        step=step,
        random_change=random_change,
        random_solution=random_solution,
        objective_function=objective_function,
        max_trials=max_trials,
    )

    evolution_strategy.run(
        generational=True,
        generation_size=100,
        best_references=50
    )

    print()

    random_search = MhRandomSearch(
        data=data,
        step=step,
        max_trials=max_trials,
        random_solution=random_solution,
        objective_function=objective_function
    )

    random_search.run()


if __name__ == '__main__':
    main()
