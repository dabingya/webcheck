# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 下午3:06
# @Author  : 大兵

import urllib.request
import json,ssl
ssl._create_default_https_context = ssl._create_unverified_context

class sendWeinxin():

    def __init__(self,name,content):
        corpid = 'ww04b751cfe15c4798'
        corpsecret = 'cT1Z_fkYOSKa8DKIARbyORo-ybJJKdOBZX62PLTsuvM'
        url = 'https://qyapi.weixin.qq.com'
        token = self.get_token(url, corpid, corpsecret)
        msg_data = self.messages(name, content)
        self.send_message(url, token, msg_data)

    # 获取企业微信token
    def get_token(self,url, corpid, corpsecret):
        token_url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (url, corpid, corpsecret)
        token = json.loads(urllib.request.urlopen(token_url).read().decode())['access_token']
        return token

    # 构建告警信息json
    def messages(self,name,msg):
        values = {
            "touser": name,
            "msgtype": 'text',
            "agentid": '1000002',
            "text": {'content': msg},
            "safe": 0
            }
        msges=(bytes(json.dumps(values), 'utf-8'))
        return msges

    # 发送告警信息
    def send_message(self,url,token, data):
            send_url = '%s/cgi-bin/message/send?access_token=%s' % (url,token)
            respone=urllib.request.urlopen(urllib.request.Request(url=send_url, data=data)).read()
            x = json.loads(respone.decode())['errcode']
            # print(x)
            if x == 0:
                print ('Succesfully')
            else:
                print ('Failed')

