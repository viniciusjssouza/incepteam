import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from input import *

app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('home.html', datasets=available_datasets())

@app.route('/team-member/<dataset>')
def team_member_csv(dataset):
    filename = './webapp/static/datasets/{0}/{0}.csv'.format(dataset)
    return read_file(filename)

@app.route('/management/<dataset>')
def management_csv(dataset):
    filename = './webapp/static/datasets/{0}/{0}_management.csv'.format(dataset)
    return read_file(filename)

@app.route('/teams/<dataset>')
def teams_csv(dataset):
    filename = './webapp/static/datasets/{0}/{0}_teams.csv'.format(dataset)
    return read_file(filename)

@app.route('/dataset/add', methods=['POST'])
def add_dataset():
    dataset = request.form['name']

    os.makedirs('./webapp/static/datasets/{}'.format(dataset))

    for f in [x.format(dataset) for x in ['{}.csv', '{}_management.csv', '{}_teams.csv']]:
        touch(f)

    return redirect('/')


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

def touch(filename):
    with open(filename, 'w') as f:
        pass

def available_datasets():
    return os.listdir('./webapp/static/datasets')

def read_file(filename):
    with open(filename) as f:
        content = f.read()
    return content


app.run(debug=True)
