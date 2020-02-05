# -*- coding:UTF-8 -*-
# Author:M9KJ-TEAM
import time
import argparse
import threading
import queue as Queue
from poc_run import autorun
from poc_manager import poc_insert_main,message

class thread_run(threading.Thread,autorun):
    def __init__(self,queue,scanMethod):
        threading.Thread.__init__(self)
        self._queue = queue
        self.scanMethod = scanMethod
    def run(self):
        while not self._queue.empty():
            target = self._queue.get()
            try:
                if self.scanMethod == '1':
                    autorun(target).aotorun()
                else:
                    autorun(target).specific(self.scanMethod)
            except Exception as e:
                print("error-【类：thread_run，函数：run】\n->参数：queue",e)
                pass
#启用多线程扫描
def poc_thread_main(type,thread_num):
    if type == 'scan':
        poc_scanMethod = input('请输入扫描方案，1.poc碰撞（请输入序号1） 2.关键词poc扫描(直接输入关键词)：')
        queue = Queue.Queue()
        try:
            f = open(r'target.txt', 'r',encoding='UTF-8')
            for line in f.readlines():
                target = line.strip('\n')
                queue.put(target)
            threads = []
            thread_count = int(thread_num)
            for i in range(thread_count):
                threads.append(thread_run(queue,poc_scanMethod))
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            f.close()
        except Exception as e:
            print("error-【函数：poc_thread_main】\n->参数：无", e)
            pass
    elif type == 'poc_manager':
        try:
            poc_managerType = int(input('请输入管理中心入口，1.poc展示（请输入序号1） 2.插入poc（请输入序号2）：'))
            if poc_managerType == 1:
                for poc in message().display_pocs():
                    print('POC-id:%s |POC-name:%s |POC-payload:%s |POC-day:%s |POC-author:%s |POC-type:%s |POC-path:%s'%(poc[0],poc[1],poc[2],poc[3],poc[4],poc[5],poc[6]))
            elif poc_managerType == 2:
                thread_count = int(thread_num)
                poc_insert_main(thread_count)
            else:
                print("error-请输入管理中心入口序号输入错误！")
        except Exception as e:
            print("error-【函数：poc_thread_main】\n->参数：无", e)
    else:
        print('【info】：type类型输入错误！')
if __name__ == '__main__':
    print("""
     ㊣版授权_POC-TESTING_v1.0_user:admin \n
     |----------/\ \n
     |  -------->>>>>>>>>>>>>>>>>>>>   \n
     |----------\/  \n
            """)
    parser = argparse.ArgumentParser(description='主程序已启动...')
    parser.add_argument('--tNum',help='线程数设置', type=int, default = 100)
    parser.add_argument('--type',help='主程序类型设置scan or poc_manager', type=str, default='scan')
    args = parser.parse_args()
    # print(args.threadNum,args.type)
    nowtime = time.time()
    poc_thread_main(args.type,args.tNum)
    print('程序用时:',time.time()-nowtime,'s',sep=' ')