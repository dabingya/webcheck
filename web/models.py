from django.db import models

# Create your models here.

# 监控网站运行状态
class Monitor_web(models.Model):

    method_choices = (
        ("get","get"),
        ("post","post"),
    )
    domain = models.URLField(verbose_name="监控域名")
    want_code = models.IntegerField(verbose_name="期待返回值")
    ret_code = models.IntegerField(verbose_name="获得的返回值",blank=True,null=True)
    keyword = models.CharField(verbose_name="期望关键字",max_length=100)
    ret_keyword = models.CharField(verbose_name="获得的返回值",max_length=100,blank=True,null=True)
    choice_method = models.CharField(default="get",max_length=20,choices=method_choices)
    para = models.CharField(verbose_name="参数",max_length=200,blank=True,null=True)
    timer = models.IntegerField(verbose_name="上次打开时间",default=0)
    curr_timer = models.IntegerField(verbose_name="检测时间",default=0)
    bussiness_line = models.ForeignKey("Bussiness_line")
    class Meta:
        verbose_name = "监控网站表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.domain


# 业务线
class Bussiness_line(models.Model):
    name = models.CharField(verbose_name="用户名",max_length=20)


# 人员
class Users(models.Model):
    name = models.CharField(verbose_name="用户名",max_length=20)
    bussiness_line = models.ForeignKey("Bussiness_line")

