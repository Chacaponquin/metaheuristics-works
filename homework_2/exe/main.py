from mh import MhHillClimb, MhEvolutionStrategy
from problemMilitaryBudget import random_change, random_solution, objective_function
from utils import read_data
from domain import Data


def main():
    data: list[Data] = read_data()
    step = 0.1

    # ejecutar escalador de colina
    hill_climb = MhHillClimb(
        step=step,
        data=data,
        random_change=random_change,
        random_solution=random_solution,
        objective_function=objective_function
    )

    hill_climb.run(max_trials=1000)

    print('\n')

    # ejecutar evolution strategy
    evolution_strategy = MhEvolutionStrategy(
        data=data,
        step=step,
        random_change=random_change,
        random_solution=random_solution,
        objective_function=objective_function
    )

    evolution_strategy.run(
        max_trials=1000,
        generational=True,
        generation_size=100,
        best_references=50
    )


if __name__ == '__main__':
    main()
