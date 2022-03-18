#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, request, render_template
from flask_babel import Babel
from datetime import datetime
import pytz

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    """
    LANGUAGES = ["en", "fr"]

@babel.localeselector
def get_locale():
    return Config.LANGUAGES[0]

@app.route("/")
def hello_world():
    """
    hello world
    """
    utc = pytz.utc

    return render_template("1-index.html", utc_zone = utc)