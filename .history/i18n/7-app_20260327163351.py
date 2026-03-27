#!/usr/bin/env python3
"""Flask application with locale and timezone selection.

This module defines a Flask app that can mock logged-in users and
select locale and timezone from URL parameters, user preferences,
or fallback defaults.
"""
from typing import Any, Dict, Optional

import pytz
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
    """Determine locale with URL, user, header, and default priority.

    Returns:
        str: A supported locale code.
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    user = getattr(g, "user", None)
    if user:
        user_locale = user.get("locale")
        if user_locale in app.config["LANGUAGES"]:
            return user_locale

    return (
        request.accept_languages.best_match(app.config["LANGUAGES"])
        or app.config["BABEL_DEFAULT_LOCALE"]
    )


def get_timezone() -> str:
    """Determine timezone with URL, user, and default priority.

    Returns:
        str: A valid timezone string.
    """
    timezone = request.args.get("timezone")
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    user = getattr(g, "user", None)
    if user:
        user_timezone = user.get("timezone")
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone,
)


@app.route("/")
def index() -> str:
    """Render the translated home page.

    Returns:
        str: Rendered home page HTML.
    """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(debug=True)
