#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Config Class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Get locale from request """
    if request.args.get('locale') == 'fr':
        return 'fr'
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def Hello():
    """
        route and an index.html
    :return:
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
