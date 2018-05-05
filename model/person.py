
class Person:

    def __init__(self, name, role, strength=1, **preferences):
        self.name = name
        self.role = role
        self.strength = strength
        self.preferences = preferences

    def __hash__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return "%s - Role: %s, Strength: %s, Preferences: %s" % (self.name, self.role, self.strength, self.preferences)

    __repr__ = __str__
