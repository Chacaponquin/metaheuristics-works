from homework_2.classes import Data
from typing import Callable


class MhLocalSearch:
    def __init__(
            self,
            data: list[Data],
            step: int,
            random_change: Callable[[list[float], float], list[float]],
            random_solution: Callable[[float], list[float]],
            objective_function: Callable[[list[float], list[Data]], float]
    ):
        self.objective_function = objective_function
        self.step = step
        self.data = data

        self.random_change = random_change
        self.random_solution = random_solution

        self.TRESHOLD = 1 # For TA and RRT
        self.OBJECTIVE_MAX = True # goal of the optimization, True: maximization, False: minimization
        self.TRIALS_BEFORE_RESTART = 50 # For Local Search, trials before restart the search
        self.CRITERION = 'TA'  # 'TA': Treshold accepting, 'RRT': Record-to-Record Travel

    def run(self, iterations: int) -> list[float]:
        best_solution: list[float] = self.random_solution(self.step)
        best_evaluation: float = self.objective_function(best_solution, self.data)
        trials_without_improvements = 0

        ref_solution = best_solution
        for i in range(iterations):
            solution: list[float] = self.random_change(ref_solution.copy(), self.step)
            evaluation: float = self.objective_function(solution, self.data)

            if self.need_to_change_reference(
                    solution=solution,
                    ref_solution=ref_solution,
                    best_solution=best_solution
            ):
                ref_solution = solution
                trials_without_improvements = 0
            else:
                trials_without_improvements += 1

                if trials_without_improvements == self.TRIALS_BEFORE_RESTART:
                    solution = self.random_solution(self.step)
                    ref_solution = solution
                    trials_without_improvements = 0

            if abs(evaluation) < abs(best_evaluation):
                best_evaluation = evaluation
                best_solution = solution

            if not bool(evaluation):
                break

        return best_solution

    def need_to_change_reference(self, solution: list[float], ref_solution: list[float], best_solution: list[float]) -> bool:
        # for Local Search: the decision about changing the reference
        eval_s: float = self.objective_function(solution, self.data)
        eval_r: float = self.objective_function(ref_solution, self.data)
        eval_b: float = self.objective_function(best_solution, self.data)

        need_to_change_reference = False
        if (self.CRITERION == 'TA') and ((self.OBJECTIVE_MAX and eval_s >= (eval_r - self.TRESHOLD)) or (not self.OBJECTIVE_MAX and eval_s <= (eval_r + self.TRESHOLD))):
            need_to_change_reference = True
        elif (self.CRITERION == 'RRT') and ((self.OBJECTIVE_MAX and eval_s >= (eval_b - self.TRESHOLD)) or (not self.OBJECTIVE_MAX and eval_s <= (eval_b + self.TRESHOLD))):
            need_to_change_reference = True

        return need_to_change_reference
