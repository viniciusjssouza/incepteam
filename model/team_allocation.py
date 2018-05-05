
class TeamAllocation:

    def __init__(self, team_name, members):
        self.team_name = team_name
        self.members = members
        self.members.sort(key=lambda x: x.name)

    def __hash__(self):
        return self.team_name

    def __eq__(self, other):
        return self.team_name == other.team_name and self.members == other.members

    def __str__(self):
        return "Team: %s   Members: %s" % (self.team_name, self.members)

    __repr__ = __str__
