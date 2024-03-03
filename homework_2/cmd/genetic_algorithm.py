from homework_2.classes import MhGeneticAlgorithm
from homework_2.utils import read_data
from homework_2.core import random_list, random_crossing, objective_function


def main():
    data = read_data()
    step = 0.1

    test_1 = MhGeneticAlgorithm(
        data=data,
        step=step,
        random_solution=random_list,
        random_combination=random_crossing,
        objective_function=objective_function
    )

    test_1.run(
        max_trials=1000,
        generational=True,
        generation_size=100,
        best_references=50
    )


if __name__ == '__main__':
    main()