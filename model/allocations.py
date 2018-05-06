from model import AllocationCost
from copy import deepcopy


class Allocations:

    def __init__(self, problem_input, team_allocations):
        self.team_allocations = team_allocations
        self.problem_input = problem_input
        self._cost = None
        self.map_people_to_team()
        self.map_team_name_to_allocation()

    def cost(self):
        return self._cost or self.calculate_cost()

    def calculate_cost(self):
        self._cost = AllocationCost(self.problem_input, self.team_allocations).value
        return self._cost

    def __copy__(self, memodict={}):
        new_team_allocations = deepcopy(self.team_allocations)
        return Allocations(self.problem_input, new_team_allocations)

    def __str__(self):
        return str(self.team_allocations) + ", cost: " + str(self.cost())

    __repr__ = __str__

    def map_people_to_team(self):
        self.people_to_team_map = {}
        for alloc in self.team_allocations:
            for person in alloc.members:
                self.people_to_team_map[person] = alloc.team_name

    def map_team_name_to_allocation(self):
        self.team_name_to_allocation = {}
        for alloc in self.team_allocations:
            self.team_name_to_allocation[alloc.team_name] = alloc
