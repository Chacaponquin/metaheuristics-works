from homework_2.classes import MhRandomWalk
from homework_2.utils import read_data
from homework_2.core import add_or_minus_one_param, random_list, objective_function


def main():
    data = read_data()
    step = 0.1

    test_1 = MhRandomWalk(
        data=data,
        step=step,
        random_change=add_or_minus_one_param,
        random_solution=random_list,
        objective_function=objective_function
    )

    test_1.run(iterations=2000)


if __name__ == '__main__':
    main()