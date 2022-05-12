#!/usr/bin/python3
"""
This is a module that contains a Flask route"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_world2():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
