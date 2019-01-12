# -*- coding: utf-8 -*-

"""
@Datetime: 2018/12/25
@Author: Zhang Yafei
"""
from flask import Blueprint,redirect,render_template
from flask.globals import request,session
from CodeStatistics.utils.get_md5 import get_md5
from datetime import timedelta
from CodeStatistics.utils.MySQLHelper import fetchone


ac = Blueprint('account', __name__, template_folder='templates', static_folder='static')


@ac.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('pwd')
    """数据库验证"""
    password = get_md5(password)
    # conn = Connect(host='localhost', user='root', password='0000', database='flask_code', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)   # 每一行是字典
    # cursor.execute("select id,username,nickname from userinfo where username=%(us)s and password=%(pw)s",{'us':username,'pw':password})
    # data = cursor.fetchone()
    data = fetchone("select id,username,nickname from userinfo where username=%(us)s and password=%(pw)s",{'us':username,'pw':password})
    if not data:
        return render_template('login.html',error='用户名或密码错误')

    session['user_info'] = {'id':data['id'],'username':data['username'],'nickname':data['nickname']}
    if request.form.get('remember'):
        session.permanent = True
        ac.permanent_session_lifetime = timedelta(days=31)

    return redirect('/home')


@ac.route('/logout')
def logout():
    del session['user_info']
    return redirect('/login')
