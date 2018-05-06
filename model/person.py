
class Person:

    def __init__(self, name, role, strength=1, preferences=None):
        self.name = name
        self.role = role
        self.strength = strength
        self.preferences = preferences or {}

    @staticmethod
    def build_person(data):
        preferences = Person.build_preference(data)
        return Person(
            data['Nome de usuário'],
            data['role'],
            strength=int(data['strength']),
            preferences=preferences
        )

    @staticmethod
    def build_preference(data):
        preferences = {}

        for k, v in data.items():
            if 'qual time' in k.lower():
                team = k.split('[')[1].strip(']')
                preferences[team] = int(v)

        return preferences

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return "%s - Role: %s, Strength: %s, Preferences: %s" % (self.name, self.role, self.strength, self.preferences)

    def __repr__(self):
        return self.name
