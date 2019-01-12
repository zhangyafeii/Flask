# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/2
@Author: Zhang Yafei
"""
import threading

import settings
import pandas as pd


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instance


class BaseAdmin():
    list_display = []


class FileReader(object, metaclass=SingletonType):
    def __init__(self):
        """
        自动读取配置文件，并读取相关文件数据
        """
        self.enable_admins = {}

    def register(self, file_name, file_path, admin_class=BaseAdmin, encoding='utf-8'):
        admin_class = admin_class()
        file_type = file_path.rsplit('.', maxsplit=1)[1]
        if hasattr(self, file_type):
            data = getattr(self, file_type)(file_path,encoding=encoding)
        else:
            raise AttributeError("fileReader have't {} file type".format(file_type))
        # if hasattr(settings,'FILE_PATH'):
        #     for file_name, file_path in settings.FILE_PATH:
        self.enable_admins[file_name] = {}
        self.enable_admins[file_name]['data'] = data
        # print(admin_class.display_columns)
        self.enable_admins[file_name]['admin_class'] = admin_class

    def csv(self, file_path, encoding):
        return pd.read_csv(file_path, encoding=encoding)

    def xlsx(self, file_path, encoding):
        return pd.read_excel(file_path, encoding=encoding)


reader = FileReader()


