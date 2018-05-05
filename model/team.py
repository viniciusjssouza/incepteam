
class Team:

    def __init__(self, name, size, **roles):
        self.name = name
        self.size = size
        self.roles = roles

    def __hash__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name