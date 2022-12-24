from django.contrib import admin
from django.urls import path, re_path, include
# from django.conf.urls import url
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.hello),
    path('login/', views.login, name="login"),
    path('hello/', views.hello),
    path('add_book/', views.add_book),
    path('select_book/', views.select_book),
    # path('testdb1/', testdb.testdb1),
    # path('testdb/', testdb.testdb),
    # path('search/', search.search),
    # path("firstapp/", include("firstapp.urls")),# 在项目名称目录下的 urls 文件里，统一将路径分发给各个 app 目录。
    # re_path(r'^articles/([0-9]{4})/$', views.articles),  # 用于正则路径，需要自己手动添加正则首位限制符号。
    # re_path(r'^index/$', views.index, name='index'),
    # re_path(r'^bio/(?P<username>\w+)/$', views.bio, name='bio'),
    # re_path(r'^weblog/', include('blog.urls')),
]
