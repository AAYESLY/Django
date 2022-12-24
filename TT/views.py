from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world ! ")


def index(request):
    return HttpResponse("index ! ")


def bio(request):
    return HttpResponse("bio ! ")


def runoob(request):
    # views_name = 10
    # return  render(request,"runoob.html", {"views_list":views_name})
    import datetime
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    now = "datetime.datetime.now()"
    num = 89
    URL = ['https://www.baidu.com', "http://www.runoob.com"]
    dict_list = {"name": "刘妍", "age": "7"}
    list_var = ["a", "b", "c", "d"]
    list_var = []
    dic_list = {"name": ["刘妍", "荆慧", " 胖亚亚"], "age": [7, 8, 9]}
    return render(request, "base.html",
                  {"time": num, "url_list": URL, "Dict": dict_list, "listvar": list_var,
                   "DIC": dic_list, "section": '12.12', "nowday": "12.12", "IMG": "MOB!!"
                   })
