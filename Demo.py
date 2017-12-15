# coding:utf-8
import os
#计算平均时间
# index=0
# for index in open('Launch_Time.txt', 'ab+'):
#     index+=index
# print index

# s = sum([1,2,3])
# print s
#计算平均时间
import linecache



#for index in open('Launch_Time.txt', 'ab+'):
    #index.replace('\n','')

count = linecache.getline('Launch_Time.txt',3)
count1 = linecache.getline('Launch_Time.txt',4)
print count.replace("\n", "")
print count1.replace("\n", "")


# Sum=0
# for index in open('Launch_Time.txt', 'ab+'):
#     result=index.replace("\n", "")
#     #Sum+=round(float(result))
#     Sum+=int(result)
# print Sum

sleeptime=0.1
Total_Time=0

Total_Time += float(sleeptime)
print Total_Time

for index in  os.popen("adb devices"):
    print ("#".join(index.replace("\n", "").split()))


'''
try:
    devices = (os.popen("adb devices").readlines()[1]).split()
    if devices[1] == 'device':
       print "devices is:%s"%devices[0]
    else:
       print "devices not found"
except Exception as e:
            print 'devices not found, %s' % (str(e))
'''

#print (os.popen('netstat -aon|findstr "4723"').read()).strip()

# for index in  os.popen('netstat -aon|findstr "4723"'):
#     if '0.0.0.0:4723' in ("#".join(index.replace("\n", "").split())):
#         print "appium exist"
#     else:
#         os.system("appium")
#         print "appium server launch!"

# appium_server = os.popen('netstat -aon|findstr "4723"').read().split()
# print appium_server[-1]

print os.popen("appium").read()


