#!/usr/bin/python3
""" Build a Flask application """
from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ return a simple hello message """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ /hbnb web page """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    # Replace underscores with spaces in the text variable
    formatted_text = escape(text).replace('_', ' ')
    return f"C {formatted_text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text="is_cool"):
    # Replace underscores with spaces in the text variable
    formatted_text = escape(text).replace('_', ' ')
    return f"Python {formatted_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    odd_or_even = "odd" if n % 2 != 0 else "even"
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
