# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/2
@Author: Zhang Yafei
"""
from Admin.file_reader import reader
from Admin.file_reader import BaseAdmin
import settings


class LabelAdmin(BaseAdmin):
    list_display = ['药品名称','评论者信息','评论时间']


class DrugAdmin(BaseAdmin):
    list_display = ['药品中文名称', '药品商品名称']


class IndictionAdmin(BaseAdmin):
    list_display = ['通用名称','商品名称','url']


reader.register(file_name='label.xlsx',file_path='BeautifulData/file/three_people_same_label.xlsx', admin_class=LabelAdmin)
reader.register(file_name='unique_chinese_name.csv',file_path='BeautifulData/file/unique_chinese_name.csv')
reader.register(file_name='drug_name.csv',file_path='BeautifulData/file/drug_name.csv', admin_class=DrugAdmin)
# reader.register_from_config(file_path=settings.FILE_PATH, admin_class=LabelAdmin)
reader.register(file_name='drug_dict.xlsx', file_path='BeautifulData/file/drug_dict.xlsx', admin_class=IndictionAdmin)