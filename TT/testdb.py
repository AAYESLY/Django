# -*- coding: utf-8 -*-

from django.http import HttpResponse

from firstapp.models import User


# 数据库操作
def save_new_user(name, age):
    test1 = User(username=name, userage=age)
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
def testdb1(request):
    test1 = User(username='liu', userage = 1)
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
def testdb(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = User.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = User.objects.filter(id=1)

    # 获取单个对象
    response3 = User.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    User.objects.order_by('username')[0:2]

    # 数据排序
    list = User.objects.order_by("userage")
    # 上面的方法可以连锁使用
    User.objects.filter(username="liuyan").order_by("id")

    # 输出所有数据
    for var in list:
        response1 +="<p>"+ var.username + " " + str(var.userage) + "</p>    "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
