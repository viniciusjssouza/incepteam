import csv

from model import Person

class CsvLoader:

    def __init__(self, filename):
        self.filename = filename
        self.csv_data = None

    def _load(self):
        with open(self.filename) as f:
            self.csv_data = [line for line in csv.DictReader(f)]

        return self.csv_data

    def data(self):
        return self.csv_data or self._load()


class PersonLoader:

    def __init__(self, people_filename, management_filename):
        self.ppl_loader = CsvLoader(people_filename)
        self.boss_loader = CsvLoader(management_filename)

        self.loaded_people = None

    def _load_people(self):
        key = 'Nome de usuário'

        ppl_data = self.ppl_loader.data()
        boss_data = self.boss_loader.data()

        if len(ppl_data) != len(boss_data):
            raise ValueError('Preference list size does not match managemente list size')

        self.loaded_people = []
        for item in ppl_data:
            boss = next(x for x in boss_data if x[key] == item[key])
            person = Person.build_person(**{**item, **boss})
            self.loaded_people.append(person)

        return self.loaded_people

    def people(self):
        return self.loaded_people or self._load_people()
