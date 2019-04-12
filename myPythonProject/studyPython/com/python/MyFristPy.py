#!/usr/bin/python3
# encoding:utf-8

""" 
    @file  MyFristPy.py
    @author zghuang
    @time 2019/4/12 9:55
    @version 3.2.2
"""
import pymysql
import os


def dblinktest():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "Root123!", "fumsdb")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT * FROM alarm")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()

    cursor.execute("describe alarm")
    tabledate = cursor.fetchall()

    i = 0
    for row in data:
        for columns in tabledate:
            # print(columns[0], end="=")
            # print(row[i])
            print("{}={}".format(columns[0], row[i]))
            i = i + 1
        print()
        i = 0
    print()

    # 关闭数据库连接
    db.close()


def filetest():
    print(os.getcwd())
    file = open(r"C:\Users\Administrator.000\Desktop\test.txt", "w")
    file.write("it is my write")
    file.newlines
    file.close()


def getamusitelang(lower, upper):
    minnum = int(lower)
    maxnum = int(upper)
    for num in range(minnum, maxnum + 1):
        summ = 0
        n = len(str(num))
        temp = num
        while temp > 0:
            digit = temp % 10
            summ += digit ** n
            temp //= 10
            # print("digit={}, summ={}, temp={}".format(digit, summ, temp))

        if num == summ:
            print(num, end=", ")


getamusitelang(1, 1000)
