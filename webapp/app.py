import os
import csv
import json
import logging

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from input import *
from model import *
from algorithm import HillClimbing

logger = logging.getLogger()

HEADERS = {
    'PREFERENCES': [
        ','.join(['Nome de usuário', '[Team 1]', '[Team 2]', '[Team 3]', '[Team 4]']) + '\n',
        ''.join([','] * 4 + ['\n'])
    ],

    'MANAGEMENT': [
        ','.join(['Nome de usuário', 'strength', 'role']) + '\n',
        ''.join([','] * 2 + ['\n'])
    ],

    'TEAMS': [
        ','.join(['name', 'size', 'role1', 'role2', 'role3']) + '\n',
        ''.join([','] * 4 + ['\n'])
    ]
}

app = Flask(__name__)


@app.route('/dataset/<dataset>/save', methods=['POST'])
def save_dataset(dataset):
    data = request.json
    write_to_file('./webapp/static/datasets/{0}/{0}.csv'.format(dataset), data['teamMembersData'])
    write_to_file('./webapp/static/datasets/{0}/{0}_management.csv'.format(dataset), data['managementData'])
    write_to_file('./webapp/static/datasets/{0}/{0}_teams.csv'.format(dataset), data['teamData'])
    return 'ok'

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

    filenames = [
        ('PREFERENCES', '{}/{}.csv'.format(dataset_dirname, dataset)),
        ('MANAGEMENT', '{}/{}_management.csv'.format(dataset_dirname, dataset)),
        ('TEAMS', '{}/{}_teams.csv'.format(dataset_dirname, dataset))
    ]

    try:
        os.makedirs(dataset_dirname)

        for t, f in filenames:
            touch(f, t)

    except FileExistsError:
        logger.warn('Attempt to create already created dataset')

    return redirect('/')


@app.route('/run', methods=['POST'])
def run():
    dataset = request.form['name']
    data_input = problem_input(dataset)

    result = format_result(json.loads(repr(x)) for x in HillClimbing(data_input).search().team_allocations)

    return render_template('/result.html', csv_data=result)


def format_result(data):
    headers = ['team_name', 'members']

    result = [headers]
    for x in data:
        result.append([x['team_name'], '\n'.join(x['members'])])

    return result


def problem_input(dataset):
    dataset_dirname = './webapp/static/datasets/{}'.format(dataset)

    data = {
        'preferences': '{}/{}.csv'.format(dataset_dirname, dataset),
        'management': '{}/{}_management.csv'.format(dataset_dirname, dataset),
        'teams': '{}/{}_teams.csv'.format(dataset_dirname, dataset)
    }

    people_loader = PersonLoader(data['preferences'], data['management'])
    teams_loader = TeamLoader(data['teams'])

    return ProblemInput(
        people=people_loader.people(),
        teams=teams_loader.teams()
    )


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
        f.writelines(HEADERS[type])


def write_to_file(filename, content):
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(content)


def available_datasets():
    return os.listdir('./webapp/static/datasets')


def read_file(filename):
    with open(filename) as f:
        content = f.read()
    return content


app.run(debug=True)
