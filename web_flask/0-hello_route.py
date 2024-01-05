#!/usr/bin/python3
"""
Starts a flask server and returns
Hello HBNB in the root route
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    The root route
    """
    return "Hello HBNB!"


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
