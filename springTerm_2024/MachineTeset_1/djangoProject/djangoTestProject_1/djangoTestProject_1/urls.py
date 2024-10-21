"""
URL configuration for djangoTestProject_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include,reverse
from django.http import HttpResponse
from home import urls
from book import views
from movie import urls


# 视图与URL的映射
def index(request):
    # 路由反转
    # 路径自带参数
    print(reverse("book_str", kwargs={"book_id":1}))
    # 查询参数传参
    print(reverse("book_detail_query_string")+"?detail")
    # 原url文件有命名空间的必须加上命名空间
    print(reverse("movie:movie_detail", kwargs={"movie_id":1}))
    return HttpResponse("Hello World")

urlpatterns = [
    path('admin/', admin.site.urls),

    # 空页面
    path("", index, name="book_index"),
    # 查询方式传递参数 http://127.0.0.1/book/?id=3&name=三国志
    path("book/", views.book_detail_query_string, name="book_detail_query_string"),
    # 路径方式传递参数 http://127.0.0.1/1
    # 可在book_id前加类型，类型包括：int,str,slug,uuid,path，其默认类型为str
    # 如果输入不是对应类型则返回404
    # str 类型：非空且不包括'/'的字符串
    path("book/<book_id>/", views.book_query_path_str),
    path("book/str/<str:book_id>/", views.book_query_path_str, name="book_str"),
    # int 类型
    path("book/int/<int:book_id>/", views.book_query_path_int, name="book_int"),
    # slug类型：数字字母'_' 和'-'
    path("book/slug/<slug:book_id>/", views.book_query_path_slug, name="book_slug"),
    # path类型：非空英文字符串
    path("book/path/<path:book_id>/", views.book_query_path_path, name="book_path"),

    path("movie/", include("movie.urls")),

    path("home/", include("home.urls")),

]
