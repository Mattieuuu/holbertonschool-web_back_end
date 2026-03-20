#!/usr/bin/env python3
"""This module starts a basic Flask app for the authentication service.

It provides routes for welcome, user registration, and login.
"""

from flask import Flask, jsonify, Response, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])


def welcome() -> Response:
    """Return a JSON response with a welcome message for the user."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])


def users() -> Response:
    """Register a new user or return error if already registered."""
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return jsonify({"message": "missing email or password"}), 400
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])


def login() -> Response:
    """Log in a user, create session, set session_id cookie, or abort 401."""
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return jsonify({"message": "missing email or password"}), 400
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    resp = jsonify({"email": email, "message": "logged in"})
    resp.set_cookie("session_id", session_id)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
