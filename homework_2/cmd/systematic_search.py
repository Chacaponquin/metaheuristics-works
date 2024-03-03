from homework_2.classes import MhSystematicSearch
from homework_2.utils import read_data
from homework_2.core import min_value_list, random_list, next_list, objective_function


def main():
    data = read_data()
    step = 0.1

    test_1 = MhSystematicSearch(
        data=data,
        step=step,
        not_random_solution=min_value_list,
        random_solution=random_list,
        not_random_change=next_list,
        objective_function=objective_function
    )

    test_1.run(
        max_trials=10000,
        systematic_s_ini=False
    )


if __name__ == '__main__':
    main()