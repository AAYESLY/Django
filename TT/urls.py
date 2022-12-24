"""TT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
# from django.conf.urls import url
from . import views, testdb, search

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.hello),
    path('runoob/', views.runoob),
    path('testdb1/', testdb.testdb1),
    path('testdb/', testdb.testdb),
    path('search/', search.search),
    path("firstapp/", include(("firstapp.urls", "firstapp"))),# 在项目名称目录下的 urls 文件里，统一将路径分发给各个 app 目录。
    # re_path(r'^articles/([0-9]{4})/$', views.articles),  # 用于正则路径，需要自己手动添加正则首位限制符号。
    # re_path(r'^index/$', views.index, name='index'),
    # re_path(r'^bio/(?P<username>\w+)/$', views.bio, name='bio'),
    # re_path(r'^weblog/', include('blog.urls')),
]
