from homework_2.classes import MhRandomSearch
from homework_2.utils import read_data


def main():
    data = read_data()
    step = 0.1

    test_1 = MhRandomSearch(data=data, step=step)
    test_1.run(iterations=2000)


if __name__ == '__main__':
    main()