import csv

from model import Person
from model import Team

class CsvSerializer:

    def __init__(self, filename):
        self.filename = filename
        self.csv_data = None

    def _load(self):
        with open(self.filename) as f:
            self.csv_data = [line for line in csv.DictReader(f)]

        return self.csv_data

    def data(self):
        return self.csv_data or self._load()
