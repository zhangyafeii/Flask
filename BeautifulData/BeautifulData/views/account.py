# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/1
@Author: Zhang Yafei
"""
from flask import Blueprint,render_template, redirect, request, session
from BeautifulData.forms import LoginForm
from settings import NICKNAME

ac = Blueprint('ac', __name__)


@ac.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    print(request.form)
    form = LoginForm(request.form)
    print(form)
    if form.validate():
        print(form.data)
        session['user'] = {'username':form.data['username'],'nickname':NICKNAME}
        return redirect('/home')
    return render_template('login.html',form=form)


@ac.route('/logout')
def logout():
    del session['user']
    return redirect('/login')