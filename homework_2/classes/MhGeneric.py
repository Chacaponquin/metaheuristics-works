import random
from homework_2.classes import Data
from homework_2.core import random_solution, function


class MhGeneric:
    def __init__(self, data: list[Data], step: int):
        self.step = step
        self.data = data

        self.OBJECTIVE_MAX = True  # goal of the optimization, True: maximization, False: minimization
        self.GENERATIONAL = False  # type of replacement in P-metaheuristics, True: generational, False: SteadyState
        self.MAX_TRIALS = 1000  # maximum number of solutions to be explored by each metaheuristic
        self.GENERATION_SIZE = 10  # number of generations, for P-metaheuristics
        self.BEST_REFERENCES = 4  # number of solutions considered in the construction of the next generation, for P-metaheuristics

    def run(self):
        solutions = []

        for i in range(self.GENERATION_SIZE):
            solution = random_solution(step=self.step)
            evaluation = function(k_data=solution, data=self.data)
            solutions = self.insert_sorted(solutions, [evaluation, solution], self.BEST_REFERENCES)

        for g in range(1, int(self.MAX_TRIALS / self.GENERATION_SIZE)):
            new_solutions = []
            for i in range(self.GENERATION_SIZE):
                parent1 = random.randint(0, self.BEST_REFERENCES)
                parent2 = random.randint(0, self.BEST_REFERENCES)

                # a combination of two of the best solutions
                solution = self.random_combination(solutions[parent1][1].copy(), solutions[parent2][1].copy())
                evaluation = function(k_data=solution, data=self.data)
                new_solutions = self.insert_sorted(new_solutions, [evaluation, solution], self.BEST_REFERENCES)

            if self.GENERATIONAL:
                solutions = new_solutions
            else:
                for i in range(self.BEST_REFERENCES):
                    evaluation, solution = new_solutions[i][0], new_solutions[i][1]
                    solutions = self.insert_sorted(solutions, [evaluation, solution], self.BEST_REFERENCES)

        best_solution = solutions[0][1]

        return best_solution

    def insert_sorted(self, list, element, first_n):  # the firstN are sorted acoording to is_better_than, element=[key,value]
        i = 0
        while i < len(list) and i < first_n and self.is_better_than(list[i][0], element[0]):
            i += 1
        list.insert(i, element)

        return list

    def is_better_than(self, evaluation1: float, evaluation2: float):
        greater1 = evaluation1 > evaluation2
        return (((evaluation1 == evaluation2)) or (self.OBJECTIVE_MAX) and greater1) or (not (self.OBJECTIVE_MAX) and not greater1)

    def random_combination(self, solution: list[float], solution_alt: list[float]):  # OX crossover for permutation. A random section from one solution and the order values from the other solution
        size = len(solution)
        start, end = sorted([random.randint(0, size - 1) for _ in range(2)])
        new_solution = [-1] * size
        new_solution[start:end + 1] = solution[start:end + 1]

        to_add = []
        for gene in solution_alt:  # get the values in solutionAlt not yet in new_solution
            if gene not in new_solution:
                to_add.append(gene)
        pos_to_add = 0
        for i, v in enumerate(new_solution):
            if v == -1:
                new_solution[i] = to_add[pos_to_add]
                pos_to_add += 1

        return new_solution
