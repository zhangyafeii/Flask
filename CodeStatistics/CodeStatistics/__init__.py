# -*- coding: utf-8 -*-

"""
@Datetime: 2018/12/25
@Author: Zhang Yafei
"""
from flask import Flask
from CodeStatistics.views.account import ac
from .views.home import index


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object('settings')
    print('create_app')
    app.register_blueprint(ac)
    app.register_blueprint(index)

    return app
