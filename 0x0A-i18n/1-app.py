#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Config Class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def Hello():
    """
        route and an index.html
    :return:
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
