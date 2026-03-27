#!/usr/bin/env python3
"""Basic Flask application configured with Babel.

This module defines a simple Flask application using Flask-Babel
with English and French language support.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Application configuration for Babel internationalization settings."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index() -> str:
    """Render the index page.

    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
