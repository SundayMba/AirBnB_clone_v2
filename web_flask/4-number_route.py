#!/usr/bin/python3
"""
    script that starts a Flask web application
    web application must be listening on 0.0.0.0, port 5000
    Routes:
        / : display "hello HBNB!"
        /hbnb: display "HBNB"
        /c/<text>: display “C ” followed by the value of the text variable
                    (replace underscore _ symbols with a space )
        /python/<text>: display "Python ", followed by the value <text>
                        variable replaced with underscore.
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


@app.route('/c/<text>')
def c_is_fun(text):
    """ route to handle request on /c/text/  """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """ route for /python/ and /python/<text>/"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ displays 'n is a Number' only if n is an integer. """
    return "{} is a Number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
