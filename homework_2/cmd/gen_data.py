import numpy as np
import csv


def gen_value() -> float:
    return np.random.randint(5, 10)


def main():
    data = []
    for year in range(2001, 2024):
        row = [year]

        for _ in range(5):
            row.append(gen_value())

        p1 = row[1]
        p2 = row[2]
        p3 = row[3]
        p4 = row[4]
        p5 = row[5]

        p_value = p1 * 0.2 + p2 * 1 + p3 * 0.6 + p4 * 0.4 + p5 * 0.5
        row.append(round(p_value, 2))

        data.append(row)

    with open('../data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


if __name__ == '__main__':
    main()
