# -*- coding:UTF-8 -*-
# Author:M9KJ-TEAM
import time
import poc_load
import mysql_control

class run:
    def __init__(self,target,name,payload,day,author,type,path):
        self.target = target
        self.name = name
        self.payload = payload
        self.day = day
        self.author = author
        self.type = type
        self.path = path
    def runit(self):
        self.load = poc_load.poctest(self.target,self.name,self.payload,self.day,self.author,self.type,self.path)
        self.load.load_poc()
class autorun:
    def __init__(self,target):
        self.target = target
    def aotorun(self):
        vulinfo = mysql_control.query_vuls_full()
        # print(vulinfo[0])
        for i in vulinfo:
            poc_run_main = run(self.target, i[1], i[2], i[3], i[4], i[5], i[6])
            poc_run_main.runit()
    def specific(self,specific_str):
        vulinfo = mysql_control.query_vuls_specific(specific_str)
        if vulinfo != None:
            for i in vulinfo:
                poc_run_main = run(self.target, i[1], i[2], i[3], i[4], i[5], i[6])
                poc_run_main.runit()
        else:
            print("error-【类：autorun，函数：specific】\n->参数：specific_str")
# if __name__ == '__main__':
#     # mysql_control.Initialization_Mysql()
#     vulinfo = mysql_control.query_vuls_full()
#     print(vulinfo[0])
#     for i in vulinfo:
#         poc_run_main = run('target',i[1],i[2],i[3],i[4],i[5],i[6])
#         poc_run_main.runit()
#     # run().runit()
# nowtime = time.time()
# f = open(r'target.txt', 'r',encoding='UTF-8')
# for line in f.readlines():
#     target = line.strip('\n')
#     autorun(target).aotorun()
# print(time.time() - nowtime, 's', sep=' ')