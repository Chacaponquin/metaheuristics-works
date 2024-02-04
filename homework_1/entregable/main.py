import random
import csv


class KData:
    LIMIT_UP = 1
    LIMIT_DOWN = 0

    def __init__(self, step: float):
        self.step = step
        self.ks = generate_solution(self.step)

    @property
    def k1(self):
        return self.ks[0]

    @property
    def k2(self):
        return self.ks[1]

    @property
    def k3(self):
        return self.ks[2]

    @property
    def k4(self):
        return self.ks[3]

    @property
    def k5(self):
        return self.ks[4]

    def change_k_values(self, error: float):
        choice = random.randint(0, 4)
        if error < 0:
            self._down_k(choice)
        else:
            self._up_k(choice)

    def _up_k(self, index: int):
        if self.ks[index] < self.LIMIT_UP:
            self.ks[index] = self.round(self.ks[index] + self.step)

    def _down_k(self, index: int):
        if self.ks[index] > self.LIMIT_DOWN:
            self.ks[index] = self.round(self.ks[index] - self.step)

    @staticmethod
    def round(value):
        return round(value, 1)


class Data:
    def __init__(self, year: int, data: list[float]):
        self.year = year,
        self.data = data


# función para generar una solución de 5 valores de K con valores entre 0 y 1 (con un paso definido, por ejemplo 0.1)
def generate_solution(step: float):
    def gen_value() -> float:
        choices = []
        value = 0.0

        while value < KData.LIMIT_UP:
            choices.append(value)
            value = KData.round(value + step)

        return random.choice(choices)

    return [gen_value() for _ in range(5)]


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


# función objetivo
def function(k_data: list[float], data: list[Data]):
    error = 0
    k1, k2, k3, k4, k5 = k_data

    for i in range(len(data)):
        if i != 0:
            p = (k1 * data[i - 1].data[0] +
                 k2 * data[i - 1].data[1] +
                 k3 * data[i - 1].data[2] +
                 k4 * data[i - 1].data[3] +
                 k5 * data[i - 1].data[4])

            error += data[i].data[5] - p

    return round(error, 4)


# Generar una solución con enfoque heurístico
def heuristic_iteration(solution: list[float]) -> list[float]:
    data = read_data()
    k_data = KData(step=0.1)
    k_data.ks = solution

    error = function(k_data.ks, data)

    # cambiar valores de K
    k_data.change_k_values(error)

    return k_data.ks.copy()


# función para evaluar una solución
def evaluate_solution(solution: list[float]) -> float:
    data = read_data()
    return function(solution, data)


if __name__ == '__main__':
    random_solution = generate_solution(0.1)

    test_solution = [0.2, 0.4, 0.1, 0.1, 0.8]
    heuristic_solution = heuristic_iteration(test_solution.copy())

    print(f'Solución aleatoria: {str(random_solution)}')
    print(f'Solución heurística: {str(test_solution)} -> {str(heuristic_solution)}')

    print(f'Error con solución aleatoria: {str(evaluate_solution(random_solution))}')
    print(f'Error con solución heurística: {str(evaluate_solution(heuristic_solution))}')


