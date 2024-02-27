import random
from homework_2.classes import Data
from homework_2.core import random_solution, function, random_change


class MhEvolutionStrategy:
    def __init__(self, data: list[Data], step: int):
        self.step = step
        self.data = data

        self.OBJECTIVE_MAX = True  # goal of the optimization, True: maximization, False: minimization
        self.GENERATIONAL = False  # type of replacement in P-metaheuristics, True: generational, False: SteadyState
        self.MAX_TRIALS = 1000  # maximum number of solutions to be explored by each metaheuristic
        self.GENERATION_SIZE = 10  # number of generations, for P-metaheuristics
        self.BEST_REFERENCES = 4  # number of solutions considered in the construction of the next generation, for P-metaheuristics

    def run(self) -> list[float]:
        solutions = []

        for i in range(self.GENERATION_SIZE):
            solution: list[float] = random_solution(step=self.step)
            evaluation: float = function(k_data=solution, data=self.data)
            solutions = self.insert_sorted(solutions, [evaluation, solution], self.BEST_REFERENCES)

        for g in range(1, int(self.MAX_TRIALS / self.GENERATION_SIZE)):
            new_solutions = []
            for i in range(self.GENERATION_SIZE):
                parent = random.randint(0, self.BEST_REFERENCES)

                # a change with respect to one of the best solutions
                solution = random_change(ks=solutions[parent][1].copy(), step=self.step)
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

