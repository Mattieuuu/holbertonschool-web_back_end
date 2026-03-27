#!/usr/bin/env python3
"""Flask application configured with Babel locale selection.

This module defines a simple Flask application using Flask-Babel
and chooses the locale from request accepted languages.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Application configuration for Babel internationalization settings."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale() -> str:
    """Determine the best matching locale for the current request.

    Returns:
        str: Matched locale code from supported languages.
    """
    return (
        request.accept_languages.best_match(app.config["LANGUAGES"])
        or app.config["BABEL_DEFAULT_LOCALE"]
    )


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index() -> str:
    """Render the index page.

    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
