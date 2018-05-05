import unittest
import tests
from algorithm.random_allocation import RandomAllocation


class TestRandomAllocation(unittest.TestCase):

    def test_generate_random_allocation_avengers(self):
        input = tests.avengers()
        random_allocation = RandomAllocation(input.people, input.teams)
        allocations = random_allocation.generate()
        print(allocations)

    def test_generate_random_allocation_two_teams(self):
        input = tests.four_people_two_teams()
        random_allocation = RandomAllocation(input.people, input.teams)
        allocations = random_allocation.generate()
        print(allocations)

if __name__ == '__main__':
    unittest.main()