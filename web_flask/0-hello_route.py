#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!' on the root route.
    
    :return: A string 'Hello HBNB!'.
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    """
    Run the Flask web application.
    The application listens on 0.0.0.0, port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
