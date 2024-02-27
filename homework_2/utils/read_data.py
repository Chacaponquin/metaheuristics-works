import csv

from homework_1.classes import Data


def read_data() -> list[Data]:
    return_data: list[Data] = []

    with open('../data.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            year = int(row[0])
            data = [float(row[i]) for i in range(1, len(row))]

            save_data = Data(data=data, year=year)
            return_data.append(save_data)

    return return_data
