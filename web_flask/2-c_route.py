#!/usr/bin/python3
"""
Starts a flask server and returns
Hello HBNB in the root route
HBNB in the hbnb route
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    The root route
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """
    The hbnb route
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
  text = text.replace("_", " ")
  return "C {}".format(text)

  
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
