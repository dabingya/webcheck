# -*- coding: utf-8 -*-
# @Time    : 2018/3/30 下午3:35
# @Author  : 大兵


from django import forms
from django.forms import fields


class DomainForm(forms.Form):
    """
    验证域名上传
    """
    domain = forms.URLField(required=True,error_messages={
        "required": "不要为空",
        'invalid': '格式错误'
    })
    keyword = forms.CharField(max_length=100,required=True,error_messages={
        "required": "不要为空"
    })
    want_code = forms.IntegerField(required=True,error_messages={
        "required": "不要为空",
        'invalid': '请输入数字'
    })


class UserForm(forms.Form):
    """
    验证人员添加
    """
    username = forms.CharField(max_length=20,required=True,error_messages={
        "required": "不要为空",
        'invalid': '太长了'
    })