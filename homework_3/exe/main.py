from mh import MhHillClimb, MhEvolutionStrategy, MhRandomSearch, MhRandomWalk
from problemMilitaryBudget import random_change, random_solution, objective_function
from heuristic import Heuristic
from utils import read_data
from domain import Data


class Instance:
    def __init__(self, step: float, data: list[Data]):
        self.step = step
        self.data = data


def main():
    data_1: list[Data] = read_data(name='data_1')
    data_2: list[Data] = read_data(name='data_2')

    instances = [
        Instance(step=0.01, data=data_1),
        Instance(step=0.05, data=data_1),
        Instance(step=0.08, data=data_1),
        Instance(step=0.1, data=data_1),
        Instance(step=0.2, data=data_1),

        Instance(step=0.01, data=data_2),
        Instance(step=0.05, data=data_2),
        Instance(step=0.08, data=data_2),
        Instance(step=0.1, data=data_2),
        Instance(step=0.2, data=data_2),
    ]

    max_trials = 1000
    times = 10

    # Random walk
    print('Camino aleatorio')
    for index, inst in enumerate(instances):
        print(f'Instancia {index + 1}')
        for i in range(times):
            random_walk = MhRandomWalk(
                data=inst.data,
                step=inst.step,
                objective_function=objective_function,
                random_solution=random_solution,
                random_change=random_change
            )

            random_walk.run(iterations=max_trials)

        print()

    # Escalador de colinas
    print('Escalador de colinas')
    for index, instance in enumerate(instances):
        print(f'Instancia {index + 1}')

        for i in range(times):
            hill_climb = MhHillClimb(
                step=instance.step,
                data=instance.data,
                random_change=random_change,
                random_solution=random_solution,
                objective_function=objective_function,
                max_trials=max_trials
            )

            hill_climb.run()

        print()

    # Evolution Strategy 1
    print('Evolution Strategy 1')
    for index, instance in enumerate(instances):
        print(f'Instancia {index + 1}')

        for i in range(times):
            evolution_strategy = MhEvolutionStrategy(
                data=instance.data,
                step=instance.step,
                random_change=random_change,
                random_solution=random_solution,
                objective_function=objective_function,
                max_trials=max_trials,
            )

            evolution_strategy.run(
                generational=False,
                generation_size=20,
                best_references=10
            )

        print()

    # Evolution Strategy 2
    print('Evolution Strategy 2')
    for index, instance in enumerate(instances):
        print(f'Instancia {index + 1}')

        for i in range(times):
            evolution_strategy = MhEvolutionStrategy(
                data=instance.data,
                step=instance.step,
                random_change=random_change,
                random_solution=random_solution,
                objective_function=objective_function,
                max_trials=max_trials,
            )

            evolution_strategy.run(
                generational=False,
                generation_size=50,
                best_references=25
            )

        print()

    # Búsqueda aleatoria
    print('Búsqueda aleatoria')
    for index, instance in enumerate(instances):
        print(f'Instancia {index + 1}')

        for i in range(times):
            random_search = MhRandomSearch(
                data=instance.data,
                step=instance.step,
                max_trials=max_trials,
                random_solution=random_solution,
                objective_function=objective_function
            )

            random_search.run()

        print()

    # Heurística
    print('Heurística')
    for index, instance in enumerate(instances):
        print(f'Instancia {index + 1}')

        for i in range(times):
            heuristic = Heuristic(
                step=instance.step,
                random_solution=random_solution,
                objective_function=objective_function,
                data=instance.data
            )

            heuristic.run(iterations=max_trials)

        print()


if __name__ == '__main__':
    main()
