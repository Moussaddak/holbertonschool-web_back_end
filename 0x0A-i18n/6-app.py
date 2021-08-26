#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """ Config Class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int) -> dict:
    """
        get user by id
    :param user_id:
    :return:
    """
    if user_id and type(user_id) in [int, str]:
        return users.get(int(user_id))


@babel.localeselector
def get_locale():
    """ Get locale from request """
    if request.args.get('locale') == 'fr' or \
            g.user and g.user.get('locale') == 'fr' or \
            request.headers.get('Accept-Language') and \
            request.headers.get('Accept-Language').split()[0][:2] == 'fr' or \
            Config.BABEL_DEFAULT_LOCALE == 'fr':
        return 'fr'
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """
        find a user
    :return:
    """
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


@app.route('/', methods=['GET'], strict_slashes=False)
def Hello():
    """
        route and an index.html
    :return:
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
