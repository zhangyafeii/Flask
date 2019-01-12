# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/5
@Author: Zhang Yafei
"""
from bs4 import BeautifulSoup
from lxml import etree


text = '<error><ret>0</ret><message></message><skey>@crypt_42d677ed_87d20caf1a6fb23a830b4e08334f6ad2</skey><wxsid>tmqszMsQ+9rm9o5X</wxsid><wxuin>2229427136</wxuin><pass_ticket>IqqqHuHFQCWvPExj%2BPNmFI7twUVx%2BG7quvAgkCyV9lgLhw73vxHSVCFMWxS9WHIf</pass_ticket><isgrayscale>1</isgrayscale></error>'


def xml_parse(text):
    result_dict = {}
    soup = BeautifulSoup(text, 'html.parser')
    result = soup.find('error').find_all()
    for tag in result:
        result_dict[tag.name] = tag.text
    return result_dict


def lxml_parse(text):
    result_dict = {}
    xml = etree.XML(text=text)
    result = xml.xpath('//error')[0].xpath('node()')
    for tag in result:
        result_dict[tag.tag] = tag.text
        # result_dict[tag.xpath('name()')] = tag.xpath('string()')
    return result_dict

"""
['__bool__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', 
'__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
 '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '_init', 'addnext', 
 'addprevious', 'append', 'attrib', 'base', 'clear', 'cssselect', 'extend', 'find', 'findall', 
 'findtext', 'get', 'getchildren', 'getiterator', 'getnext', 'getparent', 'getprevious',
  'getroottree', 'index', 'insert', 'items', 'iter', 'iterancestors', 'iterchildren', 
  'iterdescendants', 'iterfind', 'itersiblings', 'itertext', 'keys', 'makeelement', 'nsmap', 
  'prefix', 'remove', 'replace', 'set', 'sourceline', 'tag', 'tail', 'text', 'values', 'xpath']
"""

# print(__name__)   # 自己执行__name__ == __main__   外部包导入执行__name__ == utils
response_dict = {
    "BaseResponse": {
    "Ret": 0,
    "ErrMsg": ""
    },
    "AddMsgCount": 1,
    "AddMsgList": [{
    "MsgId": "7085997970647890898",
    "FromUserName": "@@1d51012ad983711b57b948e28ee2610f0a380c59598251623045ad9d14ce9b35",
    "ToUserName": "@f6ba0d841039d616b6f4652ad35e2cfb56a90beaa16316632eb7c372eec25ea5",
    "MsgType": 1,
    "Content": "@8cc4f5395f4d3057284ca6c0f5f5590501706c8a1db29df9a28f4088a35be3ed:<br/>这个是最新版的立项背景，又改了几处。",
    "Status": 3,
    "ImgStatus": 1,
    "CreateTime": 1546694346,
    "VoiceLength": 0,
    "PlayLength": 0,
    "FileName": "",
    "FileSize": "",
    "MediaId": "",
    "Url": "",
    "AppMsgType": 0,
    "StatusNotifyCode": 0,
    "StatusNotifyUserName": "",
    "RecommendInfo": {
    "UserName": "",
    "NickName": "",
    "QQNum": 0,
    "Province": "",
    "City": "",
    "Content": "",
    "Signature": "",
    "Alias": "",
    "Scene": 0,
    "VerifyFlag": 0,
    "AttrStatus": 0,
    "Sex": 0,
    "Ticket": "",
    "OpCode": 0
    }
    ,
    "ForwardFlag": 0,
    "AppInfo": {
    "AppID": "",
    "Type": 0
    }
    ,
    "HasProductId": 0,
    "Ticket": "",
    "ImgHeight": 0,
    "ImgWidth": 0,
    "SubMsgType": 0,
    "NewMsgId": 7085997970647890898,
    "OriContent": "",
    "EncryFileName": ""
    }
    ],
    "ModContactCount": 0,
    "ModContactList": [],
    "DelContactCount": 0,
    "DelContactList": [],
    "ModChatRoomMemberCount": 0,
    "ModChatRoomMemberList": [],
    "Profile": {
    "BitFlag": 0,
    "UserName": {
    "Buff": ""
    }
    ,
    "NickName": {
    "Buff": ""
    }
    ,
    "BindUin": 0,
    "BindEmail": {
    "Buff": ""
    }
    ,
    "BindMobile": {
    "Buff": ""
    }
    ,
    "Status": 0,
    "Sex": 0,
    "PersonalCard": 0,
    "Alias": "",
    "HeadImgUpdateFlag": 0,
    "HeadImgUrl": "",
    "Signature": ""
    }
    ,
    "ContinueFlag": 0,
    "SyncKey": {
    "Count": 7,
    "List": [{
    "Key": 1,
    "Val": 701699264
    }
    ,{
    "Key": 2,
    "Val": 701699333
    }
    ,{
    "Key": 3,
    "Val": 701699271
    }
    ,{
    "Key": 11,
    "Val": 701699217
    }
    ,{
    "Key": 201,
    "Val": 1546694394
    }
    ,{
    "Key": 1000,
    "Val": 1546674122
    }
    ,{
    "Key": 1001,
    "Val": 1546674196
    }
    ]
    }
    ,
    "SKey": "",
    "SyncCheckKey": {
    "Count": 7,
    "List": [{
    "Key": 1,
    "Val": 701699264
    }
    ,{
    "Key": 2,
    "Val": 701699333
    }
    ,{
    "Key": 3,
    "Val": 701699271
    }
    ,{
    "Key": 11,
    "Val": 701699217
    }
    ,{
    "Key": 201,
    "Val": 1546694394
    }
    ,{
    "Key": 1000,
    "Val": 1546674122
    }
    ,{
    "Key": 1001,
    "Val": 1546674196
    }
    ]
    }
    }


if __name__ == '__main__':
    # xml_result = xml_parse(text)
    # xml_result = lxml_parse(text)
    # print(xml_result)
    from urllib.parse import urlencode
    from urllib.parse import quote

    print(urlencode({'k1':'zhangyafei'}))
    print(quote('张亚飞'))