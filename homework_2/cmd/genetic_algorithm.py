from homework_2.classes import MhGeneticAlgorithm
from homework_2.utils import read_data


def main():
    data = read_data()
    step = 0.1

    test_1 = MhGeneticAlgorithm(data=data, step=step)
    test_1.run(
        max_trials=1000,
        generational=True,
        generation_size=100,
        best_references=50
    )


if __name__ == '__main__':
    main()