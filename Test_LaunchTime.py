# coding:utf-8
"""
Created on 17/12/14
@author: xinxi
测试点：
"""
import sys, getopt, time, os
import unittest
from Driver import AppiumWebDriver
import inspect


sleeptime = 0.1
#设置循环等待的时间
test_count = 10
#测试的次数
Timeout=10
#最大超时时间

reload(sys)
sys.setdefaultencoding('utf-8')
Sava_Path=time.strftime("%Y%m%d%H%M%S", time.localtime())\
          +'_Launch_Time.txt'
#保存文件路径

class Test_LaunchTime(unittest.TestCase):
    def test_LanuchTime(self):
        try:
            self.driver = AppiumWebDriver.new()
            start_time=str('{:.0f}'.format(time.time()*1000))#去除科学计数法
            Total_Time = 0
            # 初始化时间
            while True:
                if self.driver.current_activity == '.home.activity.HomeActivity'and \
                   self.driver.find_elements_by_android_uiautomator('text("全职招聘")'):
                   end_time=str('{:.0f}'.format(time.time()*1000))
                   diff_time=int(end_time)-int(start_time)#计算app启动耗时
                   with open(Sava_Path, 'ab+') as f:
                     f.write(str(diff_time)+'\n')
                     break

                else:
                    time.sleep(sleeptime)
                    Total_Time += float(sleeptime)
                    if Total_Time >= Timeout:
                    # 和超时时间对比,如果超时触发一个异常
                       raise Exception("Time Out!!!", Total_Time)

        except Exception as e:
            print 'setUp failed, %s' % (str(e))

    def tearDown(self):
        self.driver.quit()

#执行命令行参数封装
def main(argv):
    if check_devices() == 0:
        test_count = ''
        try:
            opts, args = getopt.getopt(argv, "ht:", ["ifile="])
        except getopt.GetoptError:
            print 'test.py -t <test_count>'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print 'test.py -t <test_count>'
                sys.exit()
            elif opt in ("-t", "--ifile"):
                test_count = arg
        return test_count


#执行具体的单元测试方法
def test_method(test_count):
    classname = Test_LaunchTime.__name__ #获取类
    methodname = Test_LaunchTime.__dict__ #获取方法名的字典
    test_count=int(test_count)
    suite=unittest.TestSuite()
    for index in  range(test_count):
        for key,value in methodname.items():
            if key != 'tearDown' and key.startswith('test'):
                print "test_method === "+key
                suite.addTest(Test_LaunchTime(key))
    unittest.TextTestRunner(verbosity=2).run(suite)

    # 计算平均时间
    Sum = 0
    f = open(Sava_Path, 'ab+')
    for index in f:
        result=index.replace("\n", "")
        Sum += int(result)
    f.write("平均测试%d次:%s毫秒"%(test_count,Sum/test_count))

# 检查设备状态
def check_devices():
    try:
        devices = (os.popen("adb devices").readlines()[1]).split()
        if devices[1] == 'device':
           print "devices is:%s"%devices[0]
           return 0
        else:
           print "devices not found"
           return 1
    except Exception as e:
        print 'devices not found, %s' % (str(e))
        return 1
# 检查appium状态
def check_appium():
    print os.popen('netstat -aon|findstr "4723"')





if __name__ == '__main__':
    test_count = main(sys.argv[1:])
    test_method(test_count)











