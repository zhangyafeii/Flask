# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/1
@Author: Zhang Yafei
"""
from flask import Blueprint, render_template, request, Markup, url_for
from BeautifulData.utils.pagination import Pagination
from Admin.file_reader import reader

main = Blueprint('main', __name__, static_folder='static')


@main.app_template_global()
def active_path(path):
    if request.path == path:
        node = '<li class="active">'
    else:
        node = '<li>'
    return Markup(node)


@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/file_list')
def file_list():
    data_list = reader.enable_admins
    page_obj = Pagination(data_list.__len__(), request.args.get('p'),per_page_num=5)
    page_str = page_obj.page_str(base_url=url_for('main.file_list'))
    data_list = [{k:data_list[k]} for k in data_list.keys()][page_obj.start:page_obj.end]
    data_list = {list(item.keys())[0]: list(item.values())[0] for item in data_list}
    return render_template('file_list.html', data_list=data_list, page_str=page_str, page_obj=page_obj)


@main.route('/data_list/<table_name>')
def data_list(table_name):
    df = reader.enable_admins[table_name]
    page_obj = Pagination(df['data'].shape[0], request.args.get('p'),per_page_num=5)
    page_str = page_obj.page_str(base_url=url_for('main.data_list', table_name=table_name))
    admin_class = df['admin_class']
    data_list = df['data'][page_obj.start:page_obj.end]
    context = {'table_name':table_name, 'data_list':data_list,
               'page_obj':page_obj, 'page_str':page_str,
               'admin_class':admin_class,
               }
    return render_template('data_list.html', **context)


@main.route('/detail/<table_name>_<int:index>')
def detail(table_name,index):
    data = reader.enable_admins[table_name]['data'].loc[index]
    return render_template('detail.html', data=data, table_name=table_name)