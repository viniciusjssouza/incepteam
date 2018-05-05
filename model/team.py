
class Team:

    def __init__(self, name, size, roles):
        self.name = name
        self.size = size
        self.roles = roles or {}

    @staticmethod
    def build_team(**data):
        name = data['name']
        size = data['size']
        roles = Team.build_roles(data)

        return Team(name, size, roles)

    @staticmethod
    def build_roles(data):
        roles = {}

        for k, v in data.items():
            if v and k not in ('name', 'size'):
                roles[k] = int(v)

        return roles

    def __hash__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return "%s - Size: %d, Roles: %s" % (self.name, self.size, self.roles)

    def __repr__(self):
        return self.name
