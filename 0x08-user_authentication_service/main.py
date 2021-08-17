#!/usr/bin/env python3
"""
End-to-end integration test Module
"""
import requests


def register_user(email: str, password: str) -> None:
    """
    :param email:
    :param password:
    :return:
    """
    body = {'email': email, 'password': password}

    response = requests.post('http://localhost:5000/users', data=body)

    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """
    :param email:
    :param password:
    :return:
    """
    body = {'email': email, 'password': password}
    response = requests.post('http://localhost:5000/sessions', data=body)
    assert response.status_code == 401


def profile_unlogged() -> None:
    """
    :return:
    """
    response = requests.get('http://localhost:5000/profile')
    assert response.status_code == 403


def log_in(email: str, password: str) -> str:
    """
    :param email:
    :param password:
    :return:
    """
    body = {'email': email, 'password': password}

    response = requests.post('http://localhost:5000/sessions', data=body)
    assert response.status_code == 200
    return requests.cookies['session_id']


def profile_logged(session_id: str) -> None:
    """
    :param session_id:
    :return:
    """
    response = requests.get('http://localhost:5000/profile', cookies=dict(session_id=session_id))
    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """
    :param session_id:
    :return:
    """

    response = requests.delete('http://localhost:5000/sessions', cookies=dict(session_id=session_id))
    assert response.status_code != 403


def reset_password_token(email: str) -> str:
    """
    :param email:
    :return:
    """
    body = {'email': email}
    response = requests.post('http://localhost:5000/reset_password', data=body)
    assert response.status_code == 200
    token = response.json()
    return token["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    :param email:
    :param reset_token:
    :param new_password:
    :return:
    """
    body = {'reset_token': reset_token,
            "new_password": new_password, "email": email}
    response = requests.put('http://localhost:5000/reset_password', data=body)
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
