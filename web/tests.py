from django.test import TestCase

# Create your tests here.


import time
#
#
#
# print(int(time.time()))
#
#
# time.sleep(10)
#
#
# print(int(time.time()))

# from web import check_url
#
#
# cc = check_url.Check_url()
#
# ret = cc.check("http://ddd.td.idnternal/","百度")
#
# print(ret)



# 测试定时任务

import schedule

import time


# def job():
#     print("i am working...")
#     print(int(time.time()))
#
#
#
# schedule.every(5).seconds.do(job)
#
#
#
# while True:
#     schedule.run_pending()
#
#     # time.sleep(1)


import requests
url = 'http://www.58pic.com'
data = {"status":0,"msg":'无数据'}
rr = requests.get(url, timeout=5)
rr.encoding = 'gbk'


print(rr.text)

