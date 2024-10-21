from django.shortcuts import render, redirect, reverse
from django.http.response import JsonResponse, HttpResponse
import random
import string
from django.core.mail import send_mail
from register.models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model, login, logout

User = get_user_model()


# Create your views here.

# csrf防御,表单中必须添加name="csrfmiddlewaretoken"
@require_http_methods(["GET", "POST"])
def login_view(reqeust):
    if reqeust.method == "GET":
        return render(reqeust, "login.html")
    else:
        form = LoginForm(reqeust.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            remember_me = form.cleaned_data.get("remember_me")
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                login(reqeust, user)

                if not remember_me:
                    # 没有记住我过期时间设置为0
                    reqeust.session.set_expiry(0)
                    return redirect("/")
            else:
                print("邮箱或密码错误")
                return redirect(reverse("register:login"))


@require_http_methods(['GET','POST'])
def register_view(reqeust):
    if reqeust.method == "GET":
        return render(reqeust, "register.html")
    else:
        form = RegisterForm(reqeust.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # 用create_user()会将密码加密后存储
            # User(email=email, username=username, password=password)创建用户直接存储
            User.objects.create_user(email=email, username=username, password=password)
            # 注册完成登录到登录界面
            return redirect(reverse("register:login"))
        else:
            print(form.errors)
            # 注册不通过重新返回注册界面
            return redirect(reverse("register:register"))

# 用/?接收邮箱
def send_captcha(reqeust):
    email = reqeust.GET["email"]
    if not email:
        # 网页返回的json中code=400则有错误
        return JsonResponse({"code": 400, "message": "必须传递邮箱"})
    else:
        # 生成四位阿拉伯数字验证码
        # ['0', '3' ,'1' , '5']
        captcha = "".join(random.sample(string.digits,k=4))
        # 将验证码更新或创建存入到数据库中
        CaptchaModel.objects.update_or_create(email=email,defaults={"captcha": captcha})
        # send_mail三个参数：主体，内容
        send_mail("个性学习空间注册表",
                  message="你的邮箱验证码是{}".format(captcha),
                  recipient_list=[email],
                  from_email=None,
        )
        print(f"{email}邮箱的验证码是：{captcha}")
        return JsonResponse({"code": 200, "message": "邮箱验证码已发送"})

def logout_view(reqeust):
    logout(reqeust)
    return redirect(reverse("register:login"))