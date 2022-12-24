from django.http import HttpResponse
from django.shortcuts import render

from TT.testdb import save_new_user


def search(request):
    request.encoding='utf-8'
    # message = 'sSSS'
    num = 89
    URL = ['https://www.baidu.com', "http://www.runoob.com"]
    dict_list = {"name": "刘妍", "age": "7"}
    list_var = ["a", "b", "c", "d"]
    list_var = []
    dic_list = {"name": ["刘妍", "荆慧", " 胖亚亚"], "age": [7, 8, 9]}
    ctx = {}
    if 'qget' in request.GET and request.GET['qget']:
        message_get = '你搜索的内容为：' + request.GET['qget']
    else:
        message_get = ''
    if 'qpost' in request.POST and request.POST['qpost']:
        save_new_user( request.POST['qpost'], request.POST['qpost2'])
        message_post = "数据添加成功！\n"
        message_post += request.POST['qpost'] + ':  '+request.POST['qpost2']
    else:
        message_post = ''
    return render(request, "base.html",
                  {"time": num, "url_list": URL, "Dict": dict_list, "listvar": list_var,
                   "DIC": dic_list, "section": '12.12', "nowday": "12.12", "IMG": "MOB!!",
                   'input_posttext': message_post, 'input_gettext': message_get
                   })
