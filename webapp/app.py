import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from input import *

HEADERS = {
    'PREFERENCES': '"Nome de usuário","[Team red]","[Team blue]","[Team green]","[Team yellow]"',
    'MANAGEMENT': 'Nome de usuário,strength,role',
    'TEAMS': 'name,size,role1,role2,role3'
}

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
    dataset_dirname = './webapp/static/datasets/{}'.format(dataset)

    os.makedirs(dataset_dirname)

    filenames = [
        ('PREFERENCES', '{}/{}.csv'.format(dataset_dirname, dataset)),
        ('MANAGEMENT', '{}/{}_management.csv'.format(dataset_dirname, dataset)),
        ('TEAMS', '{}/{}_teams.csv'.format(dataset_dirname, dataset))
    ]

    for t, f in filenames:
        touch(f, t)

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


def touch(filename, type):
    with open(filename, 'w') as f:
        f.writelines([HEADERS[type]])


def available_datasets():
    return os.listdir('./webapp/static/datasets')


def read_file(filename):
    with open(filename) as f:
        content = f.read()
    return content


app.run(debug=True)
