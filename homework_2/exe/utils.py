import csv
from domain import Data


# función para leer los datos del CSV
def read_data() -> list[Data]:
    return_data: list[Data] = []

    with open('./data.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            year = int(row[0])
            data = [float(row[i]) for i in range(1, len(row))]

            save_data = Data(data=data, year=year)
            return_data.append(save_data)

    return return_data


def insert_sorted(list, element, first_n, objective_max: bool) -> list:
    i = 0
    while (
        i < len(list) and
        i < first_n and
        is_better_than(evaluation1=list[i][0], evaluation2=element[0], objective_max=objective_max)
    ):
        i += 1

    list.insert(i, element)

    return list


def is_better_than(evaluation1: float, evaluation2: float, objective_max: bool) -> bool:
    ev1 = abs(evaluation1)
    ev2 = abs(evaluation2)
    greater1 = ev1 > ev2

    return (
        (ev1 == ev2) or
        (objective_max and greater1) or
        (not objective_max and not greater1)
    )
