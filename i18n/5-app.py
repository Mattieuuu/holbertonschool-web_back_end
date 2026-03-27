#!/usr/bin/env python3
"""Flask application with mocked login support and Babel translations.

This module defines a Flask app that can mock a logged-in user through a
URL parameter and display translated login-related messages.
"""
from typing import Any, Dict, Optional

from flask import Flask, g, render_template, request
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Application configuration for Babel internationalization settings."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


@app.before_request
def before_request() -> None:
    """Find and set a mocked user on flask global context before requests."""
    g.user = get_user()


def get_user() -> Optional[Dict[str, Any]]:
    """Retrieve a user from mock table using login_as URL parameter.

    Returns:
        Optional[Dict[str, Any]]: A user dictionary if found, otherwise None.
    """
    user_id = request.args.get("login_as")
    if user_id is None:
        return None

    try:
        return users.get(int(user_id))
    except (TypeError, ValueError):
        return None


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
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
