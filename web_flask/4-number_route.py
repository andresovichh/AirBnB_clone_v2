#!/usr/bin/python3
"""
This is a module that contains a Flask route"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ prints 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_world2():
    """ prints 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    """ returns text with 'C' """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_text_python(text="is cool"):
    """ returns text with 'C' """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if type(n) is int:
        return "{} is a number".format(n)
    else:
        return "Not a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
