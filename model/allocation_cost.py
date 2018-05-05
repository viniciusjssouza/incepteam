import statistics


class AllocationCost:

    def __init__(self, problem_input, allocations):
        self.input = problem_input
        self.allocations = allocations
        self.value = self.calculate()

    def calculate(self):
        costs = {'preference': self.preferences_cost(), 'roles': self.roles_cost(), 'strength': self.strength_cost()}
        print(costs)
        return sum(costs.values())

    def preferences_cost(self):
        total = 0
        for alloc in self.allocations:
            for person in alloc.members:
                total += pow(person.preferences[alloc.team_name], 2)
        return total

    def roles_cost(self):
        total = 0
        for alloc in self.allocations:
            roles_count = {}
            for person in alloc.members:
                roles_count[person.role] = roles_count.get(person.role, 0) + 1

            current_team = self.input.teams_by_name[alloc.team_name]
            for role, expected in current_team.roles.items():
                if roles_count.get(role, 0) < expected:
                    total += pow(len(self.input.teams), 2)
        return total

    def strength_cost(self):
        mean_strength = statistics.mean(person.strength for person in self.input.people)

        total = 0
        for alloc in self.allocations:
            expected_strength = len(alloc.members)*mean_strength
            team_strength = sum(person.strength for person in alloc.members)
            total += pow(expected_strength-team_strength, 2)
        return total
