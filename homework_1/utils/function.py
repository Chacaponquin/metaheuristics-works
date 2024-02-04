from homework_1.classes import Data


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
