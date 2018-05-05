
class ProblemInput:

    def __init__(self, people, teams):
        self.people = people
        self.teams = teams
        self.check_input()

    def check_input(self):
        if self.total_team_size() != len(self.people):
            msg = "Teams total size (%d) does not match with number of people (%d)" % (self.total_team_size(), len(self.people))
            raise ValueError(msg)

    def total_team_size(self):
        return sum(team.size for team in self.teams)