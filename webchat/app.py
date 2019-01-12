# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/4
@Author: Zhang Yafei
"""
import json

from flask import Flask, render_template, session, jsonify, request
import requests
import time
import re
from utils import xml_parse


app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = '1212sasdsadasdsad'


@app.template_global()
def get_encode_url(url):
    return url.encode('utf-8')


@app.route('/login')
def login():
    ctime = int(time.time() * 1000)
    qcode_url = 'https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}'.format(ctime)
    result = requests.get(url=qcode_url)
    qcode = re.findall('uuid = "(.*?)";',result.text)[0]
    session['qcode'] = qcode
    return render_template('login.html', qcode=qcode)


@app.route('/check_login')
def check_login():
    ctime = int(time.time() * 1000)
    qcode = session.get('qcode')
    check_url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip=0&r=-424644071&_={1}'.format(qcode, ctime)
    ret = requests.get(check_url)
    result = {'code': None}
    if 'window.code=408' in ret.text:
        # 用户未扫码
        result = {'code':408}
    elif 'window.code=201' in ret.text:
        # 用户已扫码，获取头像
        result['code'] = 201
        result['avatar'] = re.findall("window.userAvatar = '(.*)';", ret.text)[0]
    elif 'window.code=200' in ret.text:
        # 用户确认登录
        redirect_uri = re.findall('window.redirect_uri="(.*)";', ret.text)[0]
        redirect_uri = redirect_uri + '&fun=new&version=v2'
        ru = requests.get(redirect_uri)
        ticket_info = xml_parse(ru.text)
        session['ticket_info'] = ticket_info
        session['cookies'] = ru.cookies.get_dict()
        result['code'] = 200

    return jsonify(result)


@app.route('/index')
def index():
    init_url = 'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-464534318&lang=zh_CN&pass_ticket={0}'.format(session['ticket_info']['pass_ticket'])
    response = requests.post(
        url=init_url,
        json={'BaseRequest':{
                'Uin': session['ticket_info']['wxuin'],
                'Sid': session['ticket_info']['wxsid'],
                'Skey': session['ticket_info']['skey'],
                }
        })
    # print(response.text)
    response.encoding = response.apparent_encoding
    init_user_dict = response.json()
    return render_template('index.html', init_user_dict=init_user_dict)


@app.route('/get_all_contact')
def get_all_contact():
    all_contact_url = 'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&pass_ticket={pass_ticket}&r={r}&seq=0&skey={skey}'.format(pass_ticket=session['ticket_info']['pass_ticket'], r=int(time.time() * 1000), skey=session['ticket_info']['skey'])
    response = requests.get(
        url=all_contact_url,
        cookies=session['cookies'],
    )
    response.encoding = 'utf-8'
    all_users = response.json()
    return render_template('all_contact.html', all_users=all_users)


@app.route('/get_img')
def get_img():
    prev = request.args.get('prev')  # /cgi-bin/mmwebwx-bin/webwxgeticon?seq=686005187
    username = request.args.get('username')  # @9c4df5e041eb06725a410a3d9d580877e229066895b3e91d44a7af8be37e0e5b
    skey = request.args.get('skey')  # @crypt_ac8812af_a5601beadce3211cdb4fd3663d08ab52

    head_img_url = "https://wx2.qq.com{0}&username={1}&skey={2}".format(prev, username, skey)
    response = requests.get(
        url=head_img_url,
        cookies=session['cookies'],
    )
    return response.content


@app.route('/send_msg',methods=['GET','POST'])
def send_msg():
    if request.method == "GET":
        return render_template('send_msg.html')

    ctime = int(time.time() * 1000)
    from_user = request.form.get('fromUser')
    to_user = request.form.get('toUser')
    content = request.form.get('content')

    data_dict = {
        'BaseRequest': {
            'DeviceID': 'e748749962046258',
            'Sid': session['ticket_info']['wxsid'],
            'Skey': session['ticket_info']['skey'],
            'Uin': session['ticket_info']['wxuin'],
        },
        'Msg':{
            'ClientMsgId':ctime,
            'Content':content,
            'FromUserName':from_user,
            'LocalID':ctime,
            'ToUserName':to_user,
            'Type':1
        },
        'Scene': 0,
        }

    msg_url = "https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket={0}".format(session['ticket_info']['pass_ticket'])
    rep = requests.post(
        url=msg_url,
        data=bytes(json.dumps(data_dict,ensure_ascii=False),encoding='utf-8'),
    )

    print(rep)

    return "发送成功"


@app.route('/check_msg')
def check_msg():
    data_dict = {
        "BaseRequest": {
            'Sid': session['ticket_info']['wxsid'],
            'Skey': session['ticket_info']['skey'],
            'Uin': session['ticket_info']['wxuin'],
            "DeviceID": "e212384886616326",
        },
        "SyncKey": {
            "Count": 7,
            "List": [
                {"Key": 1, "Val": 701699264},
                {"Key": 2, "Val": 701699323},
                {"Key": 3, "Val": 701699271},
                {"Key": 11, "Val": 701699217},
                {"Key": 201, "Val": 1546693439},
                {"Key": 1000, "Val": 1546674122},
                {"Key": 1001, "Val": 1546674196}
            ]
        },
        "rr": -505215091,
    }
    response = requests.post(
        url='https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsync?sid={0}m&skey={1}&lang=zh_CN&pass_ticket={2}'.format(session['ticket_info']['wxsid'],session['ticket_info']['skey'],session['ticket_info']['pass_ticket']),
        json=data_dict,
    )
    response.encoding = 'utf-8'
    msg = response.json()
    print(msg["AddMsgCount"])
    result = {'status': None}
    if msg["AddMsgCount"] == 0:
        result['status'] = False
    elif msg["AddMsgCount"] >= 1:
        for content_list in msg['AddMsgList']:
            print(content_list['Content'])
        result['status'] = True
        result['content'] = msg['AddMsgList']
    return jsonify(result)


if __name__ == '__main__':
    app.run()