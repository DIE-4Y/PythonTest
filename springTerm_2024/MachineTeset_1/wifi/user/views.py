import random
import string
import json
from audioop import reverse

from django.shortcuts import HttpResponse, render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from .models import CustomUser, Stu, Teacher, Admin


@require_http_methods(["GET", "POST"])
def loginView(request):
    if request.method == 'POST':
        params = json.loads(request.body.decode())
        username = params.get('username')
        password = params.get('password')

        # 尝试在 CustomUser 表中找到用户
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"code": 200, "message": "登录成功", "id": username})
        else:
            return JsonResponse({"code": 400, "message": "用户名或密码错误"})
    else:
        return redirect(reverse('user:login'))


# @require_http_methods(["GET", "POST"])
# def loginView(request):
#     if request.method == 'POST':
#         params = json.loads(request.body.decode())
#         username = params.get('username')
#         password = params.get('password')
#
#         # user = None
#         # if Stu.objects.filter(username=username).exists():
#         #     user = Stu.objects.get(username=username)
#         # elif Teacher.objects.filter(username=username).exists():
#         #     user = Teacher.objects.get(username=username)
#         # elif Admin.objects.filter(username=username).exists():
#         #     user = Admin.objects.get(username=username)
#         #
#         # if user:
#         #     user = authenticate(username=username, password=password)
#
#         # 根据用户名查找用户
#         stu_user = Stu.objects.filter(username=username).first()
#         teacher_user = Teacher.objects.filter(username=username).first()
#         admin_user = Admin.objects.filter(username=username).first()
#
#         # 判断用户属于哪张表并进行身份验证
#         user = None
#         if stu_user:
#             user = authenticate(username=stu_user.username, password=password)
#         elif teacher_user:
#             user = authenticate(username=teacher_user.username, password=password)
#         elif admin_user:
#             user = authenticate(username=admin_user.username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return JsonResponse({"code": 200, "message": "登录成功"})
#         else:
#             return JsonResponse({"code": 400, "message": "用户名或密码错误"})
#     else:
#         return redirect(reverse('user:login'))  # 返回包含登录表单的页面


# 登出
def logoutView(request):
    logout(request)
    # 注销用户后重定向到某个页面
    return JsonResponse({"code": 200, "message": "登出成功"})


# @login_required
def addUserView(request):
    # if request.user.limit != 2:
    #     return JsonResponse({"code":"400", "message": "不是管理员不能创建用户"})
    """管理员创建用户"""
    params = json.loads(request.body.decode())
    username = params.get('username')
    password = params.get('password')
    email = params.get('email')
    name = params.get('name')
    phone_number = params.get('phone_number')
    if username and password and email and name and phone_number:
        CustomUser.objects.create(username=username, password=make_password(password), email=email,
                                  name=name, phone_number=phone_number)
        return JsonResponse({"code": 200, "message": "创建用户成功"})
    else:
        return JsonResponse({"code": 400, "message": "参数缺失"})


# @login_required
def addStuView(request):
    # if request.user.limit != 2:
    #     return JsonResponse({"code":"400", "message": "不是管理员不能创建用户"})
    """管理员创建学生"""
    params = json.loads(request.body.decode())
    username = params.get('id')
    grade = params.get('grade')
    major = params.get('major')
    age = params.get('age')
    sex = params.get('sex')
    if username and grade and major and age and sex:
        if CustomUser.objects.filter(username=username).exists():
            user = CustomUser.objects.filter(username=username).first()
            user.limit = 0
            user.save()
            Stu.objects.create(user=user, grade=grade, major=major, age=age, sex=sex)
            return JsonResponse({"code": 200, "message": "学生创建成功"})
        else:
            return JsonResponse({"code": 400, "message": "没找到该对应用户"})
    else:
        return JsonResponse({'code': 400, "message": "参数不完整"})


# @login_required
def addTeacherView(request):
    # if request.user.limit != 2:
    #     return JsonResponse({"code":"400", "message": "不是管理员不能创建用户"})
    """创建老师"""
    params = json.loads(request.body.decode())
    username = params.get('id')
    sex = params.get('sex')
    if username and sex:
        if CustomUser.objects.filter(username=username).exists():
            user = CustomUser.objects.filter(username=username).first()
            user.limit = 1
            user.save()
            Teacher.objects.create(user=user, sex=sex)
            return JsonResponse({"code": 200, "message": "老师创建成功"})
        else:
            return JsonResponse({"code": 400, "message": "没找到该对应用户"})
    else:
        return JsonResponse({'code': 400, "message": "参数不完整"})


# @login_required
def addAdminView(request):
    # if request.user.limit != 2:
    #     return JsonResponse({"code":"400", "message": "不是管理员不能创建用户"})
    """创建管理员"""
    params = json.loads(request.body.decode())
    username = params.get('id')
    if username:
        if CustomUser.objects.filter(username=username).exists():
            user = CustomUser.objects.filter(username=username).first()
            user.limit = 2
            user.save()
            Admin.objects.create(user=user)
            return JsonResponse({"code": 200, "message": "管理员创建成功"})
        else:
            return JsonResponse({"code": 400, "message": "没找到该对应用户"})
    else:
        return JsonResponse({'code': 400, "message": "参数不完整"})


# @login_required
@require_http_methods(["GET", "POST"])
def editStuView(request):
    """管理员修改学生信息"""
    if request.method == "GET":
        students = CustomUser.objects.filter(limit=0)
        student_usernames = [student.username for student in students]
        return JsonResponse({'id': student_usernames}, safe=False)
    else:
        params = json.loads(request.body.decode())
        username = params.get('id')
        password = make_password(params.get('password'))
        email = params.get('email')
        phone_number = params.get('phone_number')
        grade = params.get('grade')
        major = params.get('major')
        age = params.get('age')
        sex = params.get('sex')
        if username and password and phone_number and grade and major and age and sex:
            if CustomUser.objects.filter(username=username).exists():
                user = CustomUser.objects.filter(username=username).first()
                user.password = password
                user.email = email
                user.phone_number = phone_number
                user.save()
                student = Stu.objects.filter(user=user).first()
                student.major = major
                student.grade = grade
                student.age = int(age)
                student.sex = sex
                student.save()
                return JsonResponse({"code": 200, "message": "学生信息修改成功"})
            else:
                return JsonResponse({"code": 400, "message": "没找到该学生"})
        else:
            return JsonResponse({"code": 400, "message": "参数不完整"})


# @login_required
@require_http_methods(["GET", "POST"])
def editTeacherView(request):
    """管理员修改老师信息"""
    if request.method == "GET":
        teachers = CustomUser.objects.filter(limit=1)
        teacher_usernames = [teacher.username for teacher in teachers]
        return JsonResponse({'id': teacher_usernames}, safe=False)
    else:
        params = json.loads(request.body.decode())
        username = params.get('id')
        password = make_password(params.get('password'))
        phone_number = params.get('phone_number')
        sex = params.get('sex')
        if username and password and phone_number and sex:
            if CustomUser.objects.filter(username=username).exists():
                user = CustomUser.objects.filter(username=username).first()
                user.username = username
                user.password = password
                user.phone_number = phone_number
                user.save()
                teacher = Teacher.objects.filter(user=user).first()
                teacher.sex = sex
                teacher.save()
                return JsonResponse({"code": 200, "message": "老师信息修改成功"})
            else:
                return JsonResponse({"code": 400, "message": "没找到该老师"})
        else:
            return JsonResponse({"code": 400, "message": "参数不完整"})


# @login_required
@require_http_methods(["GET", "POST"])
def editAdminView(request):
    """管理员修改管理员信息"""
    if request.method == "GET":
        admins = CustomUser.objects.filter(limit=2)
        admin_usernames = [admin.username for admin in admins]
        return JsonResponse({'id': admin_usernames}, safe=False)
    else:
        params = json.loads(request.body.decode())
        username = params.get('id')
        password = make_password(params.get('password'))
        phone_number = params.get('phone_number')
        if username and password and phone_number:
            if CustomUser.objects.filter(username=username).exists():
                user = CustomUser.objects.filter(username=username).first()
                user.username = username
                user.password = password
                user.phone_number = phone_number
                user.save()
                return JsonResponse({"code": 200, "message": "管理员信息修改成功"})
            else:
                return JsonResponse({"code": 400, "message": "没找到该管理员"})
        else:
            return JsonResponse({"code": 400, "message": "参数不完整"})

# Create your views here.
# def user(request):
#     return HttpResponse('个人主页')


# def create_stu(request):
#     j = 2022012662
#     name_ = ['云韵', '韩雪']
#     for i in range(1, 3):
#         idd = j + 1
#         j = j + 1
#         name = name_[i - 1]
#         age = random.randint(17, 20)
#         sex = random.choice(['0', '1'])
#         grade = random.choice(['大一', '大二', '大三', '大四'])
#         major = random.choice(['计算机科学', '环境科学', '数学', '物理', '土木工程', '金融', '挖掘机驾驶', '哲学'])
#         phone = generate_phone_number()
#         email = generate_email_address()
#         stu = Stu(id=idd, name=name, email=email, grade=grade, major=major, phone_number=phone, age=age, sex=sex)
#         stu.save()
#     return HttpResponse('填充成功')


# def create_teacher(request):
#     j = 371102
#     tea_name = ['杨间', '陆阳', '萧炎', '唐三']
#     for i in range(1, 3):
#         idd = j + random.randint(1, 5)
#         name = tea_name[i - 1]
#         j = j + 1
#         phone = generate_phone_number()
#         email = generate_email_address()
#         sex = random.choice(['女', '男'])
#         tea = Teacher(id=idd, name=name, phone_number=phone, email=email, sex=sex)
#         tea.save()
#     return HttpResponse('填充成功')


# def create_admin(request):
#     admin = Admin(username='8899174', name='刘斗江')
#     admin.save()
#     admin = Admin(username='8899175', name='万原声')
#     admin.save()
#     return HttpResponse('填充成功')


# def generate_phone_number():
#     # 区号（假设是三位数字）
#     area_code = ''.join(random.choices(string.digits, k=3))
#     # 用户号（假设是八位数字）
#     subscriber_number = ''.join(random.choices(string.digits, k=8))
#     return f'{area_code}-{subscriber_number}'


# def generate_email_address():
#     # 用户名（假设是5-10位的字母和数字组合）
#     username_length = random.randint(5, 10)
#     username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
#     # 域名列表
#     domains = ['gmail.com', 'yahoo.com', 'qq.com']
#     # 随机选择一个域名
#     domain = random.choice(domains)
#     return f'{username}@{domain}'
