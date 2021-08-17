#!/usr/bin/env python3
""" a basic Flask app. """
from flask import Flask, jsonify, request, make_response, abort, redirect
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'])
def root():
    """ Basic Flask app """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """ Register user """

    # email = request.form.get("'email")
    # password = request.form.get("'password")
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or password is None:
        return None

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": "{}".format(email),
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """
        Log in
    :return:
    """
    email = request.form.get("email")
    password = request.form.get("password")
    # email = request.form.get("'email")
    # password = request.form.get("'password")

    if email is None or password is None:
        return None
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)

        if not session_id:
            abort(401)
        resp = make_response(
            jsonify({"email": email, "message": "logged in"}), 200)
        resp.set_cookie("session_id", session_id)
        return resp
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """
        Log out
    :return:
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    else:
        AUTH.destroy_session(user.id)
        return redirect("/")


@app.route('/profile', methods=['GET'])
def profile():
    """
        User profile
    :return:
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """
        Get reset password token
    :return:
    """
    email = request.form.get('email')

    if email is None:
        abort(403)
    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "reset_token": token}), 200


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """
        Update password end-point
    :return:
    """
    email = request.form.get('email')
    token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    if email is None or token is None \
            or new_password is None:
        abort(403)
    try:
        AUTH.update_password(token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception as e:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
