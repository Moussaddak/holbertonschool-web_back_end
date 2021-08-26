# !/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Hello() -> str:
    """
         route and an index.html
    :return:
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
