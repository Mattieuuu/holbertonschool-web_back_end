#!/usr/bin/env python3
"""Basic Flask application for internationalization.

This module creates a simple Flask app with a single route
that renders an HTML template with a welcome message.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Render the index page with welcome message.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
