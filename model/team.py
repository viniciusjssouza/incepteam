
class Team:

    def __init__(self, name, size, **roles):
        self.name = name
        self.size = size
        self.roles = roles

    def __hash__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return "%s - Size: %d, Roles: %s" % (self.name, self.size, self.roles)

    __repr__ = __str__
