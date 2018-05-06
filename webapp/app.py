from flask import Flask
from flask import render_template
from flask import request
from input import *
import os

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

def available_datasets():
    return os.listdir('./webapp/static/datasets')


def read_file(filename):
    with open(filename) as f:
        content = f.read()
    return content


app.run(debug=True)
