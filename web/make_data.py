# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 上午9:56
# @Author  : 大兵
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "check_web.settings")
django.setup()
import schedule
import time
from django.db.models import Q
from web.wx3 import sendWeinxin
from web.models import Monitor_web,Bussiness_line,Users
from web import check_url

# 获取数据并处理 写入数据库
def ok_data():
    # 获取所有的域名
    domain_objs = Monitor_web.objects.all()

    for domain_obj in domain_objs:
        # 取到每一个对象
        cc = check_url.Check_url()
        ret = cc.check(domain_obj.domain, domain_obj.keyword)

        # ret {'status': 200, 'msg': '取得关键字'}
        t = int(time.time())
        domain_obj.ret_code = ret['status']
        domain_obj.ret_keyword = ret['msg']
        domain_obj.curr_timer = t
        if ret['status'] == domain_obj.want_code:
            domain_obj.timer = t
        domain_obj.save()
        # 判断是否长时间不能打开
        pass_t = t - domain_obj.timer
        if pass_t > 300:
            # 发送微信
            if pass_t > 3600:
                pass_t = str(round(pass_t/3600,2)) + "小时"
            elif pass_t > 60:
                pass_t = str(round(pass_t/60,2)) + "分钟"
            else:
                pass_t = str(pass_t ) + "秒"
            send_msg = domain_obj.domain + " 已经 " + pass_t + "没有数据了..."

            # 取得要发微信的人员
            names = Users.objects.filter(Q(bussiness_line_id=domain_obj.bussiness_line_id)|Q(bussiness_line_id=1))
            if names:
                for o in names:
                    print(o.name)
                    sendWeinxin(o.name, send_msg)

while True:
    time.sleep(60)
    ok_data()

# schedule.every(1).minutes.do(ok_data)
#
# while True:
#     schedule.run_pending()
