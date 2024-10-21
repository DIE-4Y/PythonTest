from urllib import request
from django.shortcuts import render
from django.http import HttpResponse


# cookie默认在浏览器中
# session默认在数据库中
# 创建cookie
def create_cookie(request):
    response = HttpResponse("创建cookie")
    max_survive_time = 60*60*3
    response.set_cookie(key= "username", value="Assianl", max_age=max_survive_time)
    return response

def get_cookie(request):
    username = request.COOKIES.get("username")
    print(username)
    return HttpResponse("获取cookie:"+username)

def delete_cookie(request):
    response = HttpResponse("删除cookie")
    response.delete_cookie("username")
    return response

# session操作

def add_session(request):
    request.session["user_id"] ="Assinal"
    request.session.set_expiry(60*60*24)
    return HttpResponse("添加session")

def get_session(request):
    user_id = request.session.get("user_id")
    print(user_id)
    return HttpResponse("session:"+user_id)



def index_view(reqeust):
    return render(reqeust, "index.html")


def blog_detail_view(reqeust, blog_id):
    return render(reqeust, "blog_detail.html")