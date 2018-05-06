from io import StringIO

class CsvSerializer:

    def __init__(self, allocations):
        self.allocations = allocations

    def serialize(self):
        result = StringIO()
        for team_alloc in self.allocations.team_allocations:
            result.write(team_alloc.team_name)
            for member in team_alloc.members:
                result.write(", %s" % (member.name))
            result.write("\n")
        return result.getvalue()