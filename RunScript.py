#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading,time,os,sys
from Test_LaunchTime import *

exitFlag = 0

class RunScript (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting " + self.name
        if self.name == "run_appium":
            run_appium()
        if self.name == "run_test":
            run_test()
        print "Exiting " + self.name

def run_appium():
    os.system('appium')

def run_test():
    time.sleep(6)#设置等待appium server启动的时间
    print "run test start!!!"
    appium_server = os.popen('netstat -aon|findstr "4723"').read().split()
    if '0.0.0.0:4723' in appium_server:
        print "appium already launch！"
        test_count = main(sys.argv[1:])
        test_method(test_count)

        os.system("taskkill /pid %s /F"%appium_server[-1])
        #结束appium_server进程


# 创建新线程
thread1 = RunScript(1, "run_appium", 1)
thread2 = RunScript(2, "run_test", 1)

# 开启线程
thread1.start()
thread2.start()

print "Exiting Main Thread"
