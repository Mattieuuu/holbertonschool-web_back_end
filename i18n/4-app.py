#!/usr/bin/env python3
"""Flask application supporting forced locale via URL parameter.

This module defines a Flask application using Flask-Babel where the
locale can be selected from URL args or request language headers.
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
    """Determine the locale for each request.

    Returns:
        str: A supported locale code.
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

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
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
