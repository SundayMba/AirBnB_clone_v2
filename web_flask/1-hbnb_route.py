#!/usr/bin/python3
"""
    script that starts a Flask web application
    web application must be listening on 0.0.0.0, port 5000
    Routes:
        / : display "hello HBNB!"
    option strict_slashes=False must be use
"""

from flask import Flask

app = Flask(__name__)


# root route decorator
@app.route('/', strict_slashes=False)
def root():
    """ route to handle request on root route """
    return "Hello HBNB!"


# /hbnb route decorator
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ route to handle request on the hbnb route """
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
