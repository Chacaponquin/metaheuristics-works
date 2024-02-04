from homework_1.classes import KData
from .function import function
from homework_1.utils import read_data


def heuristic_iteration(solution: list[float]) -> list[float]:
    data = read_data()
    k_data = KData(step=0.1)
    k_data.ks = solution

    error = function(k_data.ks, data)
    k_data.change_k_values(error)

    return k_data.ks
