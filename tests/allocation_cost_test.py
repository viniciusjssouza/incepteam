import unittest
import tests
from model import Allocations
from algorithm.random_allocation import RandomAllocation


class TestAllocationCost(unittest.TestCase):

    def test_allocation_cost_avengers(self):
        input = tests.avengers()
        team_allocations = RandomAllocation(input.people, input.teams).generate()
        allocations = Allocations(input, team_allocations)
        print(allocations.cost())

    def test_generate_random_allocation_two_teams(self):
        input = tests.four_people_two_teams()
        random_allocation = RandomAllocation(input.people, input.teams)
        team_allocations = random_allocation.generate()
        allocations = Allocations(input, team_allocations)
        print(allocations.cost())

if __name__ == '__main__':
    unittest.main()