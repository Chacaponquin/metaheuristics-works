from homework_2.classes import MhSystematicSearch
from homework_2.utils import read_data


def main():
    data = read_data()
    step = 0.1

    test_1 = MhSystematicSearch(data=data, step=step)
    test_1.run(max_trials=10000, systematic_s_ini=False)


if __name__ == '__main__':
    main()