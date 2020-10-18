from django.shortcuts import render, HttpResponse

# Create your views here.

# 路由-视图函数: /scanhosts/
def scanhosts(request):
    return HttpResponse("自动化资产扫描")
