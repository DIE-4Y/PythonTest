from django.contrib import admin
from .models import Stu, Teacher, Admin, CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'username', 'email', 'password', 'limit')
    search_fields = ('name', 'phone_number', 'username', 'email', 'limit')


# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['username', 'password', 'name', 'grade', 'major',
#                     'phone_number', 'email', 'age', 'sex', 'limit']
#     search_fields = ['username', 'name', 'grade', 'major',
#                     'phone_number', 'email', 'age', 'sex', 'limit']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['grade', 'major', 'age', 'sex']
    search_fields = ['grade', 'major', 'age', 'sex']


# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ['username', 'password', 'name', 'phone_number', 'email', 'sex', 'limit']
#     search_fields = ['username', 'name', 'phone_number', 'email', 'sex', 'limit']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['sex']
    search_fields = ['sex']


# class AdminAdmin(admin.ModelAdmin):
#     list_display = ['username', 'name', 'password', 'phone_number', 'limit']
#     search_fields = ['username', 'name', 'phone_number', 'limit']

class AdminAdmin(admin.ModelAdmin):
    list_display = []
    search_fields = []


# admin后台注册
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Stu, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Admin, AdminAdmin)


# 修改admin管理界面
admin.site.site_title = 'WisdomFlight后台管理'
admin.site.index_title = '管理模块'
admin.site.site_header = '在线学习网站管理'