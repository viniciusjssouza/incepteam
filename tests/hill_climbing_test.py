import unittest
import tests
from model import Allocations
from algorithm import HillClimbing


class TestHillClimbing(unittest.TestCase):

    def test_search_avengers(self):
        input = tests.avengers()
        solution = HillClimbing(input).search()
        print(solution.team_allocations)
        print(solution.cost())

    def test_search_two_teams(self):
        input = tests.four_people_two_teams()
        solution = HillClimbing(input).search()
        print(solution.team_allocations)
        print(solution.cost())


if __name__ == '__main__':
    unittest.main()