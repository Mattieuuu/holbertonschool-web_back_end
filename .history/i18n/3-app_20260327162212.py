#!/usr/bin/env python3
"""Flask application configured with Babel and translated templates.

This module defines a Flask application that selects locale from
request headers and renders translatable template strings.
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
    """Determine the best locale match for the current request.

    Returns:
        str: Locale code chosen from supported languages.
    """
    return (
        request.accept_languages.best_match(app.config["LANGUAGES"])
        or app.config["BABEL_DEFAULT_LOCALE"]
    )


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index() -> str:
    """Render the translated home page.

    Returns:
        str: Rendered home page HTML.
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
