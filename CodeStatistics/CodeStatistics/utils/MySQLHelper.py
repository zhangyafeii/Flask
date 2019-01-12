# -*- coding: utf-8 -*-

"""
@Datetime: 2018/12/26
@Author: Zhang Yafei
"""
import pymysql
from settings import POOL


def connect():
    conn = POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn, cursor


def connect_close(conn, cursor):
    cursor.close()
    conn.close()


def fetchone(sql, arg=list()):
    conn, cursor = connect()
    cursor.execute(sql, arg)
    data = cursor.fetchone()
    connect_close(conn, cursor)
    return data


def fetchall(sql, arg=list()):
    conn, cursor = connect()
    cursor.execute(sql, arg)
    data = cursor.fetchall()
    connect_close(conn, cursor)
    return data


def insert(sql, arg=list()):
    conn, cursor = connect()
    row = cursor.execute(sql, arg)
    conn.commit()
    connect_close(conn, cursor)
    return row


