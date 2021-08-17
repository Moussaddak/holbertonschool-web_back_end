#!/usr/bin/env python3
""" a basic Flask app. """
from flask import Flask, jsonify, request
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

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or password is None:
        return None

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": "{}".format(email),
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
