import string
import random
import json

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import render

from .models import CaptchaModel
from user.models import CustomUser


# Create your views here.


# 发送验证码到邮箱
def send_captcha(request):
    params = json.loads(request.body.decode())
    email = params.get("email")
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



# 通过邮箱改密码
def email_update_password(request):
    params = json.loads(request.body.decode())
    email = params.get("email")
    user_captcha = params.get("user_captcha")
    password1 = params.get("password1")
    password2 = params.get("password2")

    if not (email and user_captcha and password1 and password2):
        return JsonResponse({"code": "400", "message": "参数不完整"})

    if password1 != password2:
        return JsonResponse({"code": "400", "message": "两次密码不同"})

    captcha = CaptchaModel.objects.filter(email=email).first()
    if captcha and captcha.captcha == user_captcha:
        user = None
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.filter(email=email).first() # 测试用的邮箱不够，正式使用把filter().first换为get
        if user:
            user.set_password(password1)  # 使用 set_password 方法对密码进行哈希处理
            user.save()
            return JsonResponse({"code": "200", "message": "密码修改成功"})
        else:
            return JsonResponse({"code": "400", "message": "用户不存在"})
    else:
        return JsonResponse({"code": "401", "message": "验证码错误"})

# def email_update_password(request):
#     params = json.loads(request.body.decode())
#     email = params.get("email")
#     user_captcha = params.get("user_captcha")
#     password1 = params.get("password1")
#     password2 = params.get("password2")
#
#     if not (email and user_captcha and password1 and password2):
#         return JsonResponse({"code": "400", "message": "参数不完整"})
#
#     if password1 != password2:
#         return JsonResponse({"code": "400", "message": "两次密码不同"})
#
#     captcha = CaptchaModel.objects.filter(email=email).first()
#     if captcha and captcha.captcha == user_captcha:
#         user = None
#         if Stu.objects.filter(email=email).exists():
#             user = Stu.objects.get(email=email)
#         elif Teacher.objects.filter(email=email).exists():
#             user = Teacher.objects.get(email=email)
#         elif Admin.objects.filter(email=email).exists():
#             user = Admin.objects.get(email=email)
#
#         if user:
#             user.set_password(password1)  # 使用 set_password 方法对密码进行哈希处理
#             user.save()
#             return JsonResponse({"code": "200", "message": "密码修改成功"})
#         else:
#             return JsonResponse({"code": "400", "message": "用户不存在"})
#     else:
#         return JsonResponse({"code": "401", "message": "验证码错误"})

# 通过邮箱修改邮箱
def email_update_email(request):
    params = json.loads(request.body.decode())
    oldemail = params.get("oldemail")
    newemail = params.get("newemail")
    user_captcha = params.get("user_captcha")
    # 参数验证
    if not (oldemail and newemail and user_captcha):
        return JsonResponse({"code": "400", "message": "参数不完整"})
    # 老邮箱验证码是否正确
    captcha = CaptchaModel.objects.filter(email=oldemail).first()
    if captcha and captcha.captcha == user_captcha:
        user = None
        if CustomUser.objects.filter(email=oldemail).exists():
            user = CustomUser.objects.filter(email=oldemail).first() # 测试用的邮箱不够，正式使用把first替换为get
        if user:
            user.email = newemail
            user.save()
            return JsonResponse({"code": "200", "message": "邮箱修改成功"})
        else:
            return JsonResponse({"code": "400", "message": "未找到该邮箱对应的账号"})
    else:
        return JsonResponse({"code": "401", "message": "验证码错误"})

# def password_update_password(request):
#     params = json.loads(request.body.decode())
#     oldpassword = params.get("oldpassword")
#     newpassword = params.get("newpassword")
#     username = params.get("username")
#
#     if not (oldpassword and newpassword and username):
#         return JsonResponse({"code": "400", "message": "参数不完整"})
#
#     user = None
#     if Stu.objects.filter(username=username).exists():
#         user = Stu.objects.get(username=username)
#     elif Teacher.objects.filter(username=username).exists():
#         user = Teacher.objects.get(username=username)
#     elif Admin.objects.filter(username=username).exists():
#         user = Admin.objects.get(username=username)
#
#     if user:
#         if check_password(oldpassword, user.password):  # 使用 check_password 方法安全地比较密码
#             user.set_password(newpassword)  # 使用 set_password 方法对新密码进行哈希处理
#             user.save()
#             return JsonResponse({"code": "200", "message": "密码修改成功"})
#         else:
#             return JsonResponse({"code": "400", "message": "旧密码错误"})
#     else:
#         return JsonResponse({"code": "400", "message": "用户不存在"})




# 通过密码修改密码
def password_update_password(request):
    params = json.loads(request.body.decode())
    oldpassword = params.get("oldpassword")
    newpassword = params.get("newpassword")
    username = params.get("username")

    if not (oldpassword and newpassword and username):
        return JsonResponse({"code": "400", "message": "参数不完整"})

    user = None
    if CustomUser.objects.filter(username=username).exists():
        user = CustomUser.objects.filter(username=username).first() # 测试用的邮箱不够，正式使用把first替换为get

    if user:
        if check_password(oldpassword, user.password):  # 使用 check_password 方法安全地比较密码
            user.set_password(newpassword)  # 使用 set_password 方法对新密码进行哈希处理
            user.save()
            return JsonResponse({"code": "200", "message": "密码修改成功"})
        else:
            return JsonResponse({"code": "400", "message": "旧密码错误"})
    else:
        return JsonResponse({"code": "400", "message": "用户不存在"})

# def email_update_email(request):
#     params = json.loads(request.body.decode())
#     oldemail = params.get("oldemail")
#     newemail = params.get("newemail")
#     user_captcha = params.get("user_captcha")
#     # 参数验证
#     if not (oldemail and newemail and user_captcha):
#         return JsonResponse({"code": "400", "message": "参数不完整"})
#     # 老邮箱验证码是否正确
#     captcha = CaptchaModel.objects.filter(email=oldemail).first()
#     if captcha and captcha.captcha == user_captcha:
#         user = None
#         if Stu.objects.filter(email=oldemail).exists():
#             user = Stu.objects.get(email=oldemail)
#         elif Teacher.objects.filter(email=oldemail).exists():
#             user = Teacher.objects.get(email=oldemail)
#         elif Admin.objects.filter(email=oldemail).exists():
#             user = Admin.objects.get(email=oldemail)
#
#         if user:
#             user.email = newemail
#             user.save()
#             return JsonResponse({"code": "200", "message": "邮箱修改成功"})
#         else:
#             return JsonResponse({"code": "400", "message": "未找到该邮箱对应的账号"})
#     else:
#         return JsonResponse({"code": "401", "message": "验证码错误"})



# 直接改电话
def phone_update(request):
    params = json.loads(request.body.decode())
    old_phone_number = params.get("old_phone_number")
    new_phone_number = params.get("new_phone_number")

    if not (old_phone_number and new_phone_number):
        return JsonResponse({"code": "400", "message": "请输入新电话号码和旧电话号码"})

    user = None
    if CustomUser.objects.filter(phone_number=old_phone_number).exists():
        user = CustomUser.objects.get(phone_number=old_phone_number)

    if user:
        user.phone_number=new_phone_number
        user.save()
        return JsonResponse({"code": "200", "message": "电话号码修改成功"})
    else:
        return JsonResponse({"code": "400", "message": "没找到该电话号码对应的用户"})

