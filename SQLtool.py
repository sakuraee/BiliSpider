# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:19:03 2022

@author: 13774
数据库操作
"""
import pymysql


# 创建连接
def addPic(url, tag, time, source, Time,good):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123123', db='study', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    args = (url, tag, time, source,good, Time)
    # 执行SQL，并返回收影响行数
    effect_row = cursor.execute("INSERT INTO pic VALUES (%s,%s,%s,%s,%s,0,%s)", args)
    print(effect_row)
    cursor.close()
    # 关闭连接
    conn.commit()
    conn.close()


# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))

# 执行SQL，并返回受影响行数,执行多次
# effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])
def GetTopic():
    db = pymysql.connect(host="localhost", user="root", passwd="75916747", db="study", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM topic "
    res = []
    try:
        # 执行SQL语句
        cursor.execute(sql)
        result = cursor.fetchone()
        while result != None:
            res.append(result)
            result = cursor.fetchone()
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    return res
