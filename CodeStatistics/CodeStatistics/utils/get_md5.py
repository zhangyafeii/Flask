# -*- coding: utf-8 -*-

"""
@Datetime: 2018/12/25
@Author: Zhang Yafei
"""
from hashlib import md5
import settings


def get_md5(arg):
    print(settings.SALT)
    hash = md5(settings.SALT.encode())
    hash.update(bytes(arg, encoding='utf8'))
    return hash.hexdigest()