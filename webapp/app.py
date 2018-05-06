import os
import csv

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from input import *

app = Flask(__name__)


@app.route('/dataset/<dataset>/save', methods=['POST'])
def save_dataset(dataset):
    data = request.json
    print(data)
    write_to_file('./webapp/static/datasets/{0}/{0}.csv'.format(dataset), data['teamMembersData'])
    # write_to_file('./webapp/static/datasets/{0}/{0}_management.csv'.format(dataset), data['managementData'])
    # write_to_file('./webapp/static/datasets/{0}/{0}_teams.csv'.format(dataset), data['teamData'])
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

    os.makedirs('./webapp/static/datasets/{}'.format(dataset))

    for f in [x.format(dataset) for x in ['{}.csv', '{}_management.csv', '{}_teams.csv']]:
        touch(f)

    return redirect('/')


def touch(filename):
    with open(filename, 'w') as f:
        pass


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
