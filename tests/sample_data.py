from model import *
from input import *

def sudo_data():
    preferences_filename = 'input/example/incepteam.csv'
    management_filename = 'input/example/incepteam_management.csv'
    people_loader = PersonLoader(preferences_filename, management_filename)

    teams_filename = 'input/example/teams.csv'
    teams_loader = TeamLoader(teams_filename)

    return ProblemInput(
        people=people_loader.people(),
        teams=teams_loader.teams()
    )

def zoo_data():
    preferences_filename = 'input/example/zoo.csv'
    management_filename = 'input/example/zoo_management.csv'
    people_loader = PersonLoader(preferences_filename, management_filename)

    teams_filename = 'input/example/zoo_teams.csv'
    teams_loader = TeamLoader(teams_filename)

    return ProblemInput(
        people=people_loader.people(),
        teams=teams_loader.teams()
    )

def four_people_two_teams():
    people = [
        Person(name="Joao", role="backend", strength=3, preferences={
            "estoque": 1,
            "relacionamento": 2}
        ),

        Person(name="Maria", role="front", strength=1, preferences={
            "estoque": 2,
            "relacionamento": 1}
        ),

        Person(name="Pedro", role="front", strength=2, preferences={
            "estoque": 2,
            "relacionamento": 1}
        ),

        Person(name="Jane", role="backend", strength=2, preferences={
            "estoque": 1,
            "relacionamento": 2}
        ),
    ]
    teams = [
        Team(name="estoque", size=2, roles={
            "front": 1
        }),

        Team(name="relacionamento", size=2, roles={
            "front": 1
        })

    ]
    return ProblemInput(people=people, teams=teams)


def avengers():
    people = [
        Person(name="Hulk", role="heavy", strength=3, preferences={
            "america": 2,
            "battlefield": 1,
            "stark": 3
        }),

        Person(name="America", role="fast", strength=2, preferences={
            "america": 1,
            "battlefield": 2,
            "stark": 3
        }),

        Person(name="Iron Man", role="smart", strength=2, preferences={
            "america": 3,
            "battlefield": 2,
            "stark": 1
        }),

        Person(name="Thor", role="heavy", strength=3, preferences={
            "america": 3,
            "battlefield": 1,
            "stark": 2
        }),

        Person(name="Hawkeye", role="fast", strength=1, preferences={
            "america": 1,
            "battlefield": 2,
            "stark": 3
        }),

        Person(name="Ant Man", role="fast", strength=1, preferences={
            "america": 3,
            "battlefield": 2,
            "stark": 1
        }),

        Person(name="Black Panther", role="fast", strength=2, preferences={
            "america": 2,
            "battlefield": 1,
            "stark": 3
        }),

        Person(name="Black Widow", role="fast", strength=1, preferences={
            "america": 1,
            "battlefield": 2,
            "stark": 3
        }),

        Person(name="Spider Man", role="smart", strength=1, preferences={
            "america": 3,
            "battlefield": 2,
            "stark": 1
        }),

        Person(name="Star Lord", role="smart", strength=2, preferences={
            "america": 3,
            "battlefield": 1,
            "stark": 2
        }),
    ]
    teams = [
        Team(name="america", size=3, roles={
            "fast": 2,
            'heavy': 1,
        }),

        Team(name="battlefield", size=4, roles={
            "heavy": 1
        }),

        Team(name="stark", size=3, roles={
            "smart": 2
        })

    ]
    return ProblemInput(people=people, teams=teams)
