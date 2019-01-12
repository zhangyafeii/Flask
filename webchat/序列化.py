# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/5
@Author: Zhang Yafei
"""
""""
示例一：
     requests.post(
            url=msg_url,
            json= {
                'k1':'v1',
                'k2':'垃圾'
            }
        )
    json.dumps()     ->  unicode 

示例二：
     requests.post(
            url=msg_url,
            data= json.dumps({
                'k1':'v1',
                'k2':'垃圾'
            },ensure_ascii=False)
        )
    json.dumps()     ->  unicode 

示例二：
     requests.post(
            url=msg_url,
            data= bytes(json.dumps({
                'k1':'v1',
                'k2':'垃圾'
            },ensure_ascii=False),encoding='utf-8')
        )
    json.dumps()     ->  unicode 
"""

import json

data_dict = {'username':'张亚飞', 'password':'12132313213'}

result = json.dumps(data_dict)
result2 = json.dumps(data_dict, ensure_ascii=False)
result3 = bytes(json.dumps(data_dict, ensure_ascii=False),encoding='utf-8')
print(result)
print(result2)
print(result3)

# {"username": "\u5f20\u4e9a\u98de", "password": "12132313213"}
# {"username": "张亚飞", "password": "12132313213"}
# b'{"username": "\xe5\xbc\xa0\xe4\xba\x9a\xe9\xa3\x9e", "password": "12132313213"}'