# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/1
@Author: Zhang Yafei
"""
USERNAME = 'zhangyafei'
# PASSWORD = 'ZhangYafei@123'
PASSWORD = '666666'
NICKNAME = '张亚飞'

INSTALLED_APPS = (
    'BeautifulData',
)


class BaseConfig():
    DEBUG = True
    SECRET_KEY = 'assadadsadsddadasda'


class ProConfig(BaseConfig):
    pass


FILE_PATH = (
        ['label.xlsx','BeautifulData/file/three_people_same_label.xlsx'],
        ['drug_name.csv','E:/爬虫/project/药品商品名通用名称/unique_chinese_name.csv']
)