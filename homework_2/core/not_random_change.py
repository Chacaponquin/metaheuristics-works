from .not_random_solution import not_random_solution


def not_random_change(solution: list[float], max_value: float, min_value: float, step: float):
    j = 4
    while (solution[j] == max_value) and j >= 0:
        j -= 1

    if j == -1:
        solution = not_random_solution(min_value=min_value)
    else:
        solution[j] += step
        if solution[j] > max_value:
            solution[j] = max_value
        for j in range(j + 1, 5):
            solution[j] = min_value

    return solution
