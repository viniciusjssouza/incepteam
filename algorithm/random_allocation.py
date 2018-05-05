import random
from model.team_allocation import TeamAllocation


class RandomAllocation:

    def __init__(self, people, teams):
        self.people = people
        self.teams = teams

    def generate(self):
        indexes = range(0, len(self.people))
        random.shuffle(indexes)

        allocations = self.create_empty_allocations()

        current_team = 0
        for i in indexes:
            allocations[current_team].members.append(self.people[i])
            current_team = (current_team + 1) & len(self.teams)

    def create_empty_allocations(self):
        allocations = []
        for team in self.teams:
            alloc = TeamAllocation(team.name, [])
            allocations.append(alloc)
        return allocations
