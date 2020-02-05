# -*- coding:UTF-8 -*-
# Author:M9KJ-TEAM
import xlrd
import threading
import mysql_control
import queue as Queue

class poc_insert_thread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue
    def run(self):
        while not self._queue.empty():
            pocs = self._queue.get()
            message().insert_pocs(pocs)


class message:
    def __init__(self):
        pass
    def display_pocs(self):
        data = mysql_control.query_vuls_full()
        return data
    def insert_pocs(self,pocs):
        # mysql_control.insert_vul(name, payload, day, author, type, path)
        mysql_control.insert_vul(pocs[0],pocs[1],pocs[2],pocs[3],pocs[4],pocs[5])


def poc_insert_main(thread_num):
    threads = []
    queue = Queue.Queue()
    data = xlrd.open_workbook('poc_upload.xlsx')
    # 第1个sheet
    table = data.sheets()[0]
    # 获取行数
    nrows = table.nrows
    if nrows > 0:
        for i in range(nrows):
            # 第i行第j列
            print('正在插入:',str(table.row_values(i)[0]).strip())
            name = str(table.row_values(i)[0]).strip()
            payload = str(table.row_values(i)[1]).strip()
            day = str(table.row_values(i)[2]).strip()
            author = str(table.row_values(i)[3]).strip()
            type = str(table.row_values(i)[4]).strip()
            path = str(table.row_values(i)[5]).strip()
            pocs = [name,payload,day,author,type,path]
            queue.put(pocs)
    else:
        print('error-【类：message，函数：insert_pocs】\n->参数：user,day,vul_name,method,result,path，错误原因：excel无数据')
    thread_count = int(thread_num)
    for i in range(thread_count):
        threads.append(poc_insert_thread(queue))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
