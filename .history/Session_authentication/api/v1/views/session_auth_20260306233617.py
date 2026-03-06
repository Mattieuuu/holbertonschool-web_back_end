#!/usr/bin/env python3
""" Module of Session Authentication views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """ POST /api/v1/auth_session/login
    Handle user login via session authentication
    Return:
      - User object JSON represented with session cookie set
      - 400 if email or password is missing
      - 404 if no user found
      - 401 if wrong password
    """
    email = request.form.get('email')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    # Search for user by email
    users = User.search({"email": email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    # Validate password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create session ID
    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    # Create response with user data
    response = jsonify(user.to_json())

    # Set cookie
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)

    return response
