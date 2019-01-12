# -*- coding: utf-8 -*-

"""
@Datetime: 2018/12/25
@Author: Zhang Yafei
"""
import os
import uuid
import datetime
from flask import Blueprint, render_template, redirect, session, url_for, request, Markup
import shutil
from CodeStatistics.utils.MySQLHelper import fetchone,fetchall,insert


index = Blueprint('index',__name__)


@index.before_request
def authentication():
    # print('anth')
    if not session.get('user_info'):
        return redirect(url_for('account.login'))
    return None


@index.app_template_global()
def active_path(path):
    if request.path == path:
        node = '<li class="active">'
    else:
        node = '<li>'
    return Markup(node)


@index.route('/home')
def home():
    return render_template('home.html')


@index.route('/user_list')
def user_list():
    # conn = pymysql.Connect(host='localhost', user='root', password='0000', database='flask_code', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 每一行是字典
    # cursor.execute("select id,username,nickname from userinfo")
    # data = cursor.fetchall()
    data = fetchall("select userinfo.id,nickname,ifnull(sum(line),0) as line from record right join userinfo on userinfo.id=record.user_id group by userinfo.id order by line desc")
    return render_template('user_list.html',data=data)


@index.route('/detail/<int:nid>')
def detail(nid):
    # conn = pymysql.Connect(host='localhost', user='root', password='0000', database='flask_code', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 每一行是字典
    # # cursor.execute("select record.lines,record.ctime,userinfo.nickname from record inner join userinfo on record.user_id=userinfo.id where userinfo.id=%(id)s",{'id':nid})
    # cursor.execute("select record.id,record.line,record.ctime,userinfo.nickname from record,userinfo where record.user_id=userinfo.id and userinfo.id=%(id)s",{'id':nid})
    # record_list = cursor.fetchall()
    record_list = fetchall("select record.id,record.line,record.ctime,userinfo.nickname from record,userinfo where record.user_id=userinfo.id and userinfo.id=%(id)s",{'id':nid})
    empty = False
    lines = list(map(lambda x:x['line'], record_list))
    ctime = list(map(lambda x:x['ctime'].strftime("%Y.%m.%d"), record_list))
    if not record_list:
        # cursor.execute('select nickname from userinfo where id=%s',(nid,))
        # record_list = cursor.fetchall()
        record_list = fetchall('select nickname from userinfo where id=%s',(nid,))
        empty = True
        return render_template('data_list.html',record_list=record_list,empty=empty)
    return render_template('data_list.html',record_list=record_list, empty=empty, lines=lines, ctime=ctime)


@index.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    file_obj = request.files.get('code')
    # 1.检查上传文件后缀名
    file_suffix = file_obj.filename.rsplit('.',maxsplit=1)
    if file_suffix.__len__() != 2 or file_suffix[1] != 'zip':
        return render_template('upload.html',error='请上传zip文件')
    # print(file_obj.filename)
    # print(file_obj.stream)
    """
    # 2. 接收用户上传文件,并写入到服务器本地.
    file_path = os.path.join("files",file_obj.filename)
    # 从file_obj.stream中读取内容，写入到文件
    file_obj.save(file_path)

    # 3. 解压zip文件
    import shutil
    # 通过open打开压缩文件，读取内容再进行解压。
    shutil._unpack_zipfile(file_path,'xsadfasdfasdf')
    """
    # 2+3  接收用户上传文件，并解压到指定目录
    target_path = os.path.join('files', str(uuid.uuid4()))
    shutil.unpack_archive(file_obj.stream, target_path, format='zip')

    # 4.遍历某目录下的所有文件
    # for item in os.listdir(target_path):
    #     print(item)

    total_num = 0
    for base_dir,folder_list,file_list in os.walk(target_path):
        for file_name in file_list:
            file_path = os.path.join(base_dir,file_name)
            file_ext = file_path.rsplit('.', maxsplit=1)
            if len(file_ext) != 2:
                continue
            if file_ext[1] != 'py':
                continue
            file_num = 0
            with open(file_path, 'rb') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith(b'#'):
                        continue
                    file_num += 1
            total_num += file_num
            # print(file_path, total_num)

    lines, ctime, user_id = total_num, datetime.date.today(), session['user_info']['id']
    # print(lines, ctime, user_id)
    # conn = pymysql.Connect(host='localhost', user='root', password='0000', database='flask_code', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("select id from record where ctime=%s", (ctime,))
    # data = cursor.fetchone()
    data = fetchone("select id from record where ctime=%s", (ctime,))
    if data:
        return '今天已经上传'
    # cursor.execute("insert into record(line,ctime,user_id) values(%s,%s,%s)", (lines, ctime, user_id))
    # conn.commit()
    # cursor.close()
    # conn.close()
    insert("insert into record(line,ctime,user_id) values(%s,%s,%s)", (lines, ctime, user_id))
    return '上传成功'