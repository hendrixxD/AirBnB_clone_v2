#!/usr/bin/python3
"""AirBnB flask app Module"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def return_message():
    """return a simple message"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def return_HBNB():
    """return HBNB in /hbnb route"""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
