# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/1
@Author: Zhang Yafei
"""
from flask import Flask
from BeautifulData.views.account import ac
from BeautifulData.views.backend import main


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.ProConfig')

    app.register_blueprint(ac)
    app.register_blueprint(main)

    return app