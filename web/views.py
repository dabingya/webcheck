from django.shortcuts import render
import json
import time
from .models import Monitor_web,Bussiness_line,Users
from .forms import DomainForm,UserForm
from django.shortcuts import render,HttpResponse,redirect

# 首页
def index(request):

    domain_objs = Monitor_web.objects.all()

    webtime = domain_objs.last().curr_timer
    current_time = int(time.time())
    ctime = current_time - webtime


    red = "#449d44"
    green = "#ce0606"

    return render(request,'index.html',{
        "domain_objs":domain_objs,
        "color_red": red,
        "color_green":green,
        "ctime": ctime,
    })


# 增加检测域名
def add_domain(request):
    if request.method == "GET":
        # 获得所有的业务线
        bussiness_line_objs = Bussiness_line.objects.all()



        return render(request,'add_domain.html',{
            "bussiness_line_objs":bussiness_line_objs
        })
    else:

        domain_form = DomainForm(request.POST)
        bussiness_line_objs = Bussiness_line.objects.all()
        if domain_form.is_valid():
            timer = int(time.time())
            domain = request.POST.get("domain")
            keyword = request.POST.get("keyword")
            want_code = request.POST.get("want_code")
            bussiness_line = request.POST.get("bussiness_line")

            Monitor_web.objects.create(domain=domain,want_code=want_code,keyword=keyword,
                                       choice_method="get",timer=timer,curr_timer=timer,
                                       bussiness_line_id=bussiness_line)
            return redirect('/')
        else:

            return render(request,'add_domain.html',{
                "domain_form": domain_form,
                "error": domain_form.errors,
                "bussiness_line_objs": bussiness_line_objs
            })


# 增加用户
def add_user(request):
    if request.method == "GET":
        # 获得所有的业务线
        bussiness_line_objs = Bussiness_line.objects.all()

        return render(request,'add_user.html',{
            "bussiness_line_objs":bussiness_line_objs
        })
    else:
        bussiness_line_objs = Bussiness_line.objects.all()
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = request.POST.get("username")
            bussiness_line = request.POST.get("bussiness_line")

            Users.objects.create(name=username,bussiness_line_id=bussiness_line)
            return redirect('/')

        else:


            return render(request, 'add_user.html', {
                "user_form": user_form,
                "error": user_form.errors,
                "bussiness_line_objs": bussiness_line_objs
            })