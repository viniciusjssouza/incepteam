from algorithm import RandomAllocation
from model import Allocations
from copy import copy
import itertools


class HillClimbing:
    DEFAULT_N_ITERATIONS = 1000

    def __init__(self, problem_input, n_iterations=DEFAULT_N_ITERATIONS):
        self.input = problem_input
        self.n_iterations = n_iterations
        self.solution = None

    def search(self):
        self.solution = None
        for it in range(0, HillClimbing.DEFAULT_N_ITERATIONS):
            allocations = self.generate_initial_allocation()
            while True:
                new_allocations = self.improve_allocation(allocations)
                if new_allocations is None:
                    self.update_best_solution(allocations)
                    break
                else:
                    allocations = new_allocations
        return self.solution

    def improve_allocation(self, allocation):
        new_allocation = copy(allocation)
        indexes = list(range(0, len(new_allocation.team_allocations)))
        for team1, team2 in itertools.combinations(indexes, 2):
            for person1, person2 in self.combine_people(new_allocation, team1, team2):
                self.swap_people(new_allocation.team_allocations, team1, person1, team2, person2)
                if new_allocation.calculate_cost() < allocation.cost():
                    return new_allocation
                # return to the original positions
                self.swap_people(new_allocation.team_allocations, team1, person2, team2, person1)

    def swap_people(self, team_allocations, team1, person1, team2, person2):
        team_allocations[team1].members.remove(person1)
        team_allocations[team2].members.remove(person2)
        team_allocations[team1].members.add(person2)
        team_allocations[team2].members.add(person1)

    def combine_people(self, allocation, team1, team2):
        return itertools.product(allocation.team_allocations[team1].members, allocation.team_allocations[team2].members)

    def generate_initial_allocation(self):
        random_allocation = RandomAllocation(self.input.people, self.input.teams).generate()
        return Allocations(self.input, random_allocation)

    def update_best_solution(self, allocations):
        if self.solution is None or self.solution.cost() > allocations.cost():
            self.solution = allocations
