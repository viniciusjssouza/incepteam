from flask import Flask
from flask import render_template
from input import *
import os

app = Flask(__name__)


@app.route('/')
def render_home():
    return render_template('home.html', datasets=available_datasets())


@app.route('/team-member/<dataset>')
def team_member_dataset(dataset):
    preferences_filename = './webapp/static/datasets/{}.csv'.format(dataset)
    management_filename = './webapp/static/datasets/{}_management.csv'.format(dataset)
    teams_filename = './webapp/static/datasets/{}_teams.csv'.format(dataset)

    preferences_data = read_file(preferences_filename)

    data = {
        'preferences_data': read_file(preferences_filename),
        'management_data': read_file(management_filename),
        'teams_data': read_file(teams_filename)
    }
    return preferences_data


def available_datasets():
    return os.listdir('./webapp/static/datasets')


def read_file(filename):
    with open(filename) as f:
        content = f.read()
    return content


app.run(debug=True)
