# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 上午8:54
# @Author  : 大兵

import  requests

class Check_url:

    def __init__(self):
        pass

    def check(self,url,keyword):
        try:
            data = {"status":0,"msg":'无数据'}
            rr = requests.get(url, timeout=5)
            rr.encoding = 'utf-8'

            # print(rr.text)
            # rr = str(rr)
            data["status"] = rr.status_code
            if keyword in str(rr.text):
                data["msg"] = "取得关键字"
            # if want_code == rr.status_code:
            #     data["status"] = rr.status_code



        except Exception as e:
            data = {"status": 0, "msg": '无数据'}
            e = str(e)
            # 判断什么类型
            if "nodename" in e:
                data["msg"] = "不能解析"
            elif "refused" in e:
                data["msg"] = "拒绝连接"
            elif "timed out" in e:
                data["msg"] = "连接超时"
            elif "redirects" in e:
                data["msg"] = "重定向次数过大"
            else:
                data["msg"] = "未知错误"

        # print(data["status"])
        # print(type(data["status"]))
        # if data["status"] != 200:
        #     print(url+data["msg"])


        return data
