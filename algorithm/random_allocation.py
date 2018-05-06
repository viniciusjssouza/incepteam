import random
from model.team_allocation import TeamAllocation


class RandomAllocation:

    def __init__(self, people, teams):
        self.people = people
        self.teams = teams

    def generate(self):
        indexes = list(range(0, len(self.people)))
        random.shuffle(indexes)

        allocations = self.create_empty_allocations()

        for i, team in enumerate(self.teams):
            while len(allocations[i].members) < team.size:
                allocations[i].members.add(self.people[indexes.pop()])
        return allocations

    def create_empty_allocations(self):
        allocations = []
        for team in self.teams:
            alloc = TeamAllocation(team.name, [])
            allocations.append(alloc)
        return allocations

