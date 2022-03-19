#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, request, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    """
    get local lang
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def hello_world():
    """
    hello world
    """

    return render_template("3-index.html")
