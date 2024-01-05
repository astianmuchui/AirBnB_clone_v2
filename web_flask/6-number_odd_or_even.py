#!/usr/bin/python3
"""
Starts a flask server and returns
Hello HBNB in the root route
HBNB in the hbnb route
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    The root route
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
  """The hbnb route"""

  return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
  """
  The C route
  """
  
  text = text.replace("_", " ")
  return "C {}".format(text)

@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
  """
  The python route
  """  

  text = text.replace("_", " ")
  return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
  """
  The number route
  """
  
  return "{} is a number".format(n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
  """
  The number odd or even route
  """
  return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)

