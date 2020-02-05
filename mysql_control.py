# -*- coding:UTF-8 -*-
# Author:M9KJ-TEAM
import pymysql
"""
    创建数据库：
        create database if not exists db_herbal_medicine;
    创建表：
        CREATE TABLE IF NOT EXISTS `mem_cardtype_resource` (
        ...
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
"""


def Initialization_Mysql():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP DATABASE IF EXISTS vuldetail;")
    cursor.execute("CREATE DATABASE vuldetail;")
    cursor.execute("USE vuldetail;")
    # 使用预处理语句创建表
    sql = """CREATE TABLE IF NOT EXISTS `vuls` ( 
          `id` int(22) NOT NULL AUTO_INCREMENT, 
          `vul_name` varchar(255) NOT NULL, 
          `vul_payload` varchar(255) NOT NULL, 
          `vul_day` varchar(255) NOT NULL, 
          `vul_author` varchar(255) NOT NULL, 
          `vul_type` varchar(255) NOT NULL, 
          `vul_path` varchar(255) NOT NULL, 
          PRIMARY KEY (`id`) 
        ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
    cursor.execute(sql)
    db.commit()
    sql = """ALTER TABLE `vuls` ADD unique(`vul_name`)"""
    cursor.execute(sql)
    db.commit()
    sql = """CREATE TABLE IF NOT EXISTS `scan_log` ( 
          `id` int(22) NOT NULL AUTO_INCREMENT, 
          `scan_user` varchar(255) NOT NULL, 
          `scan_day` varchar(255) NOT NULL, 
          `scan_vulname` varchar(255) NOT NULL, 
          `scan_method` varchar(255) NOT NULL, 
          `scan_result` varchar(255) NOT NULL, 
          `scan_path` varchar(255) NOT NULL, 
          PRIMARY KEY (`id`) 
        ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
    cursor.execute(sql)
    db.commit()
    # 关闭数据库连接
    db.close()

def insert_vul(name,payload,day,author,type,path):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "vuldetail")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = """INSERT INTO vuls(vul_name,vul_payload,vul_day,vul_author,vul_type,vul_path) 
           VALUES ('%s','%s','%s','%s','%s','%s')""" % (name,payload,day,author,type,path)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print('error-【函数：insert_vul】\n->参数：vul_name,vul_payload,vul_day,vul_author,vul_type,vul_path',e)
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()

def insert_scan_log(user,day,vulname,method,result,path):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "vuldetail")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = """INSERT INTO scan_log(scan_user,scan_day,scan_vulname,scan_method,scan_result,scan_path) 
           VALUES ('%s','%s','%s','%s','%s','%s')""" % (user,day,vulname,method,result,path)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print('error-【函数：insert_scan_log】\n->参数：user,day,vulname,method,result,path')
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()

def query_vuls_full():
    sql = """select * from vuls; """
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "vuldetail")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # print(results)
        return results
    except Exception as e:
        print("error-【函数：query_vuls_full】\n->参数：无", e)
        return None
    db.close()

def query_vuls_specific(specific_str):
    sql = """select * from vuls where vul_path like '%{}%'; """.format(specific_str)
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "vuldetail")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print(results)
        return results
    except Exception as e:
        print("error-【函数：query_vuls_full】\n->参数：无", e)
        return None
    db.close()

def query_scan_log():
    sql = """select * from scan_log; """
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "vuldetail")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print(results)
        return results
    except Exception as e:
        print("error-【函数：query_scan_log】\n->参数：无", e)
        return None
    db.close()
