import datetime
import time
import random

import MySQLdb as mysql
import pymysql
from pymysql.constants.FIELD_TYPE import SET

fp = open("C:/Users/Sun/Desktop/tu/girl.jpg",'rb')
img = fp.read()
fp.close()

def createdb():
    con = pymysql.connect(host="localhost", port=3306, user="root", password="", db="dba")
    cursor = con.cursor()
    cursor2 = con.cursor()
    cursor3 = con.cursor()
    sql0 = """ CREATE TABLE IF NOT EXISTS `EM` (
                 FIRST_NAME  INT(20) NOT NULL,
                 LAST_NAME  CHAR(20)
                 )"""
    cursor.execute(sql0)
    sql1 = """ CREATE TABLE IF NOT EXISTS `EM1` (
                 FIRST_NAME  INT(20) NOT NULL,
                 LAST_NAME  CHAR(20)
                 )"""
    cursor2.execute(sql1)
    sql2 = """ CREATE TABLE IF NOT EXISTS `EM2` (
                 FIRST_NAME  INT(20) NOT NULL,
                 LAST_NAME  CHAR(20)
                 )"""
    cursor3.execute(sql2)

def randomtimes(start, end, n, frmt="%Y-%m-%d %H:%M:%S"):
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    time_datetime=[random.random() * (etime - stime) + stime for _ in range(n)]
    time_str=[t.strftime(frmt) for t in time_datetime]
    msg=''.join(time_str)
    print(msg)
    return msg

def writedata():
    con = pymysql.connect(host="localhost", port=3306, user="root", password="", db="dba")
    cursor = con.cursor()
    ndt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dt = randomtimes('2020-11-30 10:20:00', '2020-11-30 11:00:00', 1)
    # cursor.execute("Insert into em1(a) values(%s)", (mysql.Binary(img)))
    cursor.execute("insert into em1  select * from em where timestampdiff(second ,now(),em.start_time)< 5&&timestampdiff(second ,now(),em.start_time)>0")
    con.commit()

def interval():
    createdb()
    while 1:
        writedata()

        time.sleep(3)

if __name__ == '__main__':
    interval()
