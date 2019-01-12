# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/2
@Author: Zhang Yafei
"""
import settings
from importlib import import_module


def admin_auto_discover():
    for app_name in settings.INSTALLED_APPS:
        try:
            __import__('{}.admin'.format(app_name))
        except:
            try:
                import_module('{}.admin'.format(app_name))
            except Exception as e:
                print(e)