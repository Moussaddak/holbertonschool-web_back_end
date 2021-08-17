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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
