# -*- coding: utf-8 -*-

"""
@Datetime: 2018/12/25
@Author: Zhang Yafei
"""
"""1.加密"""
# import hashlib
#
# md5 = hashlib.md5(b'zhang')
# md5.update(bytes('666666',encoding='utf8'))
# ret = md5.hexdigest()
# print(ret)

"""2.数据库操作"""
# import pymysql
#
# conn = pymysql.Connect(host='localhost', user='root', password='0000', database='flask_code', charset='utf8')
#
# # cursor = conn.cursor()   # 每一行是元组
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)   # 每一行是字典

# sql = "select * from userinfo where username='{0}' and password='{1}'".format('zhangsan','317bc264bfd3d562fa415dbb905e2d8a')
# sql注入
# sql = "select * from userinfo where username='{0}' and password='{1}'".format("xx ' or 1=1 -- ",'317bc264bfd3d562fa415dbb905e2d8a')
# sql = "select * from userinfo where username='%s' and password ='%s'" %("xiao ' or 1=1 -- ","47f5abdd7f4083f0cc5c94d587fa3ca4")
# print(sql)
# cursor.execute(sql)
# cursor.execute("select * from userinfo where username=%s and password=%s",("xx ' or 1=1 --",'317bc264bfd3d562fa415dbb905e2d8a'))
# cursor.execute("select * from userinfo where username=%s and password=%s",('zhangsan','317bc264bfd3d562fa415dbb905e2d8a'))
# cursor.execute("select * from userinfo where username=%(us)s and password=%(pw)s",{'us':'zhangsan','pw':'317bc264bfd3d562fa415dbb905e2d8a'})
# cursor.execute("select id,username,password from userinfo where username=%(us)s and password=%(pw)s",{'us':'zhangsan','pw':'317bc264bfd3d562fa415dbb905e2d8a'})


# data = cursor.fetchall()
# data = cursor.fetchone()
#
# print(data['id'],data['username'])
#
# cursor.close()
# conn.close()

"""3.解压"""
# import shutil
#
# # 压缩文件
# shutil.make_archive('files/rabbitmq','zip','E:/Web框架/rabbitmq')
# # 解压缩
# shutil.unpack_archive(r'E:/Web框架/Flask/project/CodeStatistics/CodeStatistics/files/用户登录程序.zip',r'CodeStatisti

"""4.xpath的text和string"""
from lxml import etree

content = "<book><author>Tom <em>John</em> cat</author><pricing><price>20</price><discount>0.8</discount></pricing></book>"
response = etree.XML(text=content)
# print(response)
print(response.xpath('/book/author/text()'))
print(response.xpath('/book/author')[0].xpath('string()'))
print(response.xpath('/book/author/node()'))
print(response.xpath('/book/author/data()'))


