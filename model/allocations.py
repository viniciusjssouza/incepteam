from model import AllocationCost


class Allocations:

    def __init__(self, problem_input, team_allocations):
        self.team_allocations = team_allocations
        self.problem_input = problem_input
        self._cost = None

    def cost(self):
        return self._cost or self.calculate_cost()

    def calculate_cost(self):
        self._cost = AllocationCost(self.problem_input, self.team_allocations)
        return self._cost
