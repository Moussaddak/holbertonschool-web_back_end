#!/usr/bin/env python3
""" Module of Users views
"""
from flask import request, jsonify, abort
from models.user import User
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
        POST /api/v1/auth_session/login
    Returns:

    """
    user_email = request.form.get("email")
    user_pwd = request.form.get("password")
    if not user_email:
        return jsonify({"error": "email missing"}), 400
    if not user_pwd:
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": user_email})
    if not len(users):
        return jsonify({"error": "no user found for this email"}), 404
    user = users[0]
    if not user.is_valid_password(user_pwd):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    user_id = user.id

    session_id = auth.create_session(user_id)
    _user = jsonify(user.to_json())
    import os
    _user.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return _user


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def delete_and_logout_session() -> str:
    """ DELETE /api/v1/auth_session/logout
    """
    from api.v1.app import auth
    return (jsonify({}), 200) if auth.destroy_session(request) else abort(404)
