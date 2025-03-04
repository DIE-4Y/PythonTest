import json
import string
import random
import os
import uuid
import hashlib

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.utils import timezone

from user.models import User, Captcha
from book.models import Book, BookUser, Article, ArticleUser

app_name = 'user'


def sendCaptcha(request):
    """发送验证码"""
    params = json.loads(request.body.decode())
    email = params.get("email")
    if not email:
        return JsonResponse({"code": 809, "message": "必须传递邮箱!"})
    else:
        # 生成四位阿拉伯数字验证码['0', '3' ,'1' , '5']
        code = "".join(random.sample(string.digits, k=4))
        # 将验证码更新或创建存入到数据库中
        Captcha.objects.update_or_create(email=email, defaults={"code": code})
        # send_mail三个参数：主体，内容
        send_mail("尊敬的用户",
                  message="您的邮箱验证码是：{}".format(code),
                  recipient_list=[email],
                  from_email=None,
                  )
        return JsonResponse({"code": 709, "message": "邮箱验证码已发送"})


def register(request):
    """注册"""
    # 获取相关信息
    data = json.loads(request.body.decode())
    email = data.get('email')
    password = data.get('password')
    code = data.get('code')
    # 验证邮箱和验证码
    captcha = get_object_or_404(Captcha, email=email)
    if captcha.code == code:
        # 删除对应的验证码记录
        captcha.delete()
        # 创建用户 基于email生成username
        username = email.split('@')[0]
        user = User.objects.filter(username=username).first()
        if user:
            return JsonResponse({"code": 707, "message": "该邮箱不能创建用户！"})
        else:
            user = User(username=username, email=email, password=make_password(password))
            user.save()
            for book in Book.objects.all():
                bookuser = BookUser(book=book, user_id=user.username, status=0)
                bookuser.save()
            bookusers = BookUser.objects.filter(user_id=username)
            bookuser = random.choice(bookusers)
            bookuser.status = 1
            book = bookuser.book
            bookuser.save()
            for article in Article.objects.filter(book_id=book.id):
                articleuser = ArticleUser(article=article, book=book, user_id=user.username)
                articleuser.save()
            return JsonResponse({'code': 809, 'data': '用户创建成功'})
    else:
        return JsonResponse({'code': 709, 'message': '验证码不正确'})


def userLogin(request):
    """用户名登录"""
    data = json.loads(request.body.decode())
    username = data.get("username")
    password = data.get("password")
    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        book_id = BookUser.objects.filter(user_id=username, status=1).first().book.id
        return JsonResponse(
            {'code': 700, 'id': username, 'data': '登录成功', 'book_id': book_id, 'nailong': user.nailong,
             'coin': user.coin})
    else:
        return JsonResponse({'code': 800, 'message': '用户名或密码错误！'})


def emailLogin(request):
    """邮箱密码登录"""
    data = json.loads(request.body.decode())
    email = data.get("email")
    password = data.get("password")
    user = User.objects.filter(email=email).first()
    username = user.username
    if not user:
        return JsonResponse({'code': 800, 'message': '该邮箱未注册！'})
    if check_password(password, user.password):
        login(request, user)
        book_id = BookUser.objects.filter(user_id=username, status=1).first().book.id
        return JsonResponse(
            {'code': 700, 'id': username, 'data': '登录成功', 'book_id': book_id, 'nailong': user.nailong,
             'coin': user.coin})
    return JsonResponse({'code': 800, 'message': '密码错误！'})


def captchaLogin(request):
    """邮箱验证码登录"""
    data = json.loads(request.body.decode())
    email = data.get("email")
    code = data.get("code")

    user = User.objects.filter(email=email).first()
    username = user.username
    if not user:
        return JsonResponse({'code': 800, 'message': '该用户还未注册！'})
    captcha = Captcha.objects.filter(email=email).first()
    if captcha.code != code:
        return JsonResponse({"code": 800, "message": "验证码错误"})

    login(request, user)
    book_id = BookUser.objects.filter(user_id=username, status=1).first().book.id
    return JsonResponse({'code': 700, 'id': username, 'data': '登录成功', 'book_id': book_id, 'nailong': user.nailong,
                         'coin': user.coin})


def userLogout(request):
    """登出"""
    logout(request)
    return JsonResponse({'code': 200, 'data': "登出成功！"})


def emailUpdatePassword(request):
    """通过邮箱改密码"""
    data = json.loads(request.body.decode())
    email = data.get("email")
    user_code = data.get("code")
    password1 = data.get("password1")
    password2 = data.get("password2")
    # 参数校验
    if not (email and user_code and password1 and password2):
        return JsonResponse({"code": "801", "message": "参数不完整"})
    if password1 != password2:
        return JsonResponse({"code": "801", "message": "两次密码不同"})
    captcha = Captcha.objects.filter(email=email).first()
    if captcha and captcha.code == user_code:
        if User.objects.filter(email=email).exists():
            user = User.objects.filter(email=email).first()
            user.set_password(password1)
            user.save()
            return JsonResponse({"code": "703", "message": "密码修改成功"})
        else:
            return JsonResponse({"code": "801", "message": "用户不存在"})
    else:
        return JsonResponse({"code": "801", "message": "验证码错误"})


def passwordUpdatePassword(request):
    """通过密码修改密码"""
    params = json.loads(request.body.decode())
    oldpassword = params.get("oldpassword")
    newpassword1 = params.get("newpassword1")
    newpassword2 = params.get("newpassword2")
    username = params.get("username")

    if not (oldpassword and newpassword1 and username and newpassword2):
        return JsonResponse({"code": "803", "message": "参数不完整"})

    if User.objects.filter(username=username).exists():
        user = User.objects.filter(username=username).first()
        # 使用 check_password 方法安全地比较密码
        if check_password(oldpassword, user.password):
            if newpassword1 == newpassword2:
                # 使用 set_password 方法对新密码进行哈希处理
                user.set_password(newpassword1)
                user.save()
                return JsonResponse({"code": "705", "message": "密码修改成功"})
            return JsonResponse({"code": "803", "message": "两次密码不同"})
        return JsonResponse({"code": "803", "message": "旧密码错误"})
    return JsonResponse({"code": "803", "message": "用户不存在"})


def emailUpdateEmail(request):
    """通过邮箱修改邮箱"""
    params = json.loads(request.body.decode())
    oldemail = params.get("oldemail")
    newemail = params.get("newemail")
    user_code = params.get("code")
    # 参数验证
    if not (oldemail and newemail and user_code):
        return JsonResponse({"code": "805", "message": "参数不完整"})
    # 老邮箱验证码是否正确
    captcha = Captcha.objects.filter(email=oldemail).first()
    if captcha and captcha.code == user_code:
        if User.objects.filter(email=oldemail).exists():
            user = User.objects.filter(email=oldemail).first()
            user.email = newemail
            user.save()
            return JsonResponse({"code": "706", "message": "邮箱修改成功"})
        else:
            return JsonResponse({"code": "805", "message": "未找到该邮箱对应的账号"})
    else:
        return JsonResponse({"code": "805", "message": "验证码错误"})


def updateName(request):
    """修改名称"""
    data = json.loads(request.body.decode())
    name = data.get("name")
    username = data.get("username")
    if User.objects.filter(username=username).exists():
        user = User.objects.filter(username=username).first()
        user.name = name
        user.save()
        return JsonResponse({'code': '707', 'data': '名字修改成功！'})
    return JsonResponse({'code': '807', 'message': '该用户不存在！'})


def getRandomStr():
    """给图片生成随机名字"""
    # 获取uuid的随机数
    uuid_val = uuid.uuid4()
    # 获取uuid的随机数字符串
    uuid_str = str(uuid_val).encode('utf-8')
    # 获取md5实例
    md5 = hashlib.md5()
    # 拿取uuid的md5摘要
    md5.update(uuid_str)
    # 返回固定长度的字符串
    return md5.hexdigest()


def uploadPhoto(request):
    """接收上传的文件"""
    username = request.POST.get('username')
    recieve_pic = request.FILES.get('picture')
    if not recieve_pic:
        return JsonResponse({'code': 807, 'message': '图片不存在'})
    # 给文件一个唯一的名字 uuid + hash
    name = getRandomStr()
    file_path = os.path.join(settings.MEDIA_ROOT, name + os.path.splitext(recieve_pic.name)[1])
    # 写入到本地磁盘
    try:
        # 把图片名保存到数据库
        if not User.objects.filter(username=username).exists():
            return JsonResponse({'code': '807', 'message': "未找到该用户！"})
        user = User.objects.filter(username=username).first()
        user.photo = name + os.path.splitext(recieve_pic.name)[1]
        user.save()
        # 图片写入本地--返回图片名
        with open(file_path, 'wb') as fp:
            for i in recieve_pic.chunks():
                fp.write(i)
        return JsonResponse({'code': 708, 'data': file_path})
    except Exception as e:
        return JsonResponse({'code': 807, 'message': '图片写入失败:' + str(e)})


def getInfor(request):
    """获取用户信息"""
    try:
        username = request.GET.get('username')
        user = User.objects.get(username=username)
        return JsonResponse({'code': 200, 'data': user})
    except Exception as e:
        return JsonResponse({'code': 400, 'msg': '没找到对应用户' + str(e)})


def updateNainong(request):
    """奶龙小开关"""
    data = json.loads(request.body.decode())
    username = data['username']
    user = User.objects.get(username=username)

    if user.nailong == 1:
        user.nailong = 0
        user.save()
        return JsonResponse({'code': 708, 'data': '奶龙状态已改为关闭'})

    else:
        user.nailong = 1
        user.save()
        return JsonResponse({'code': 708, 'data': '奶龙状态已改为开启'})


def userSignIn(request):
    """签到领硬币"""
    data = json.loads(request.body.decode())
    username = data['username']
    user = User.objects.get(username=username)
    if (user.date != timezone.now().date()):
        user.recitation = 0
        coin = user.coin + 3
        user.coin = coin
        user.save()
        return JsonResponse({'code': 709, 'data': '签到成功，硬币+3！', 'coin': user.coin, 'recitation': user.recitation})
    return JsonResponse({'code': 809, 'message': '已经登陆过了', 'coin': user.coin, 'recitation': user.recitation})


def setGaol(request):
    """设置目标"""
    data = json.loads(request.body.decode())
    username = data['username']
    goal = data['goal']
    user = User.objects.filter(username=username).first()
    user.goal = goal
    user.save()
    return JsonResponse({'code': 709, 'data': '目标设置成功'})
