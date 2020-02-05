# -*- coding:UTF-8 -*-
# Author:M9KJ-TEAM
import importlib
import datetime
import mysql_control
"""
    设计思路
    导入IP或者URL | poc类型
    返回漏洞{漏洞名称 漏洞利用方式（漏洞url 漏洞payload） 漏洞是否存在 }
    扫描记录与扫描结果入数据库
"""

class poctest:
    def __init__(self,target,name,payload,day,author,type,path):
        self.target = target
        self.name = name
        self.payload = payload
        self.day = day
        self.author = author
        self.type = type
        self.path = path
    def load_poc(self):
        poc_path = importlib.import_module(self.path)
        poc_return = poc_path.run(self.target)
        print('\
 |-----------------------|\n \
|目标地址：-->%s\n \
|是否存在漏洞：-->%s\n \
|漏洞名称：-->%s\n \
|漏洞载荷：-->%s\n \
|漏洞类型：-->%s\n \
|-----------------------|\n \
        '%(self.target,poc_return,self.name,self.payload,self.type))
        mysql_control.insert_scan_log(self.author,datetime.datetime.now(),self.name,self.type,poc_return,self.path)


