from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.

class CustomUser(AbstractUser):
    # 通用用户属性
    limit_choice=(
        (0, "student"),
        (1, "teacher"),
        (2, "admin")
    )
    name = models.CharField(max_length=10, default="admin", verbose_name="姓名")
    phone_number = models.CharField(unique=True, max_length=11, verbose_name="电话号码",)
    limit = models.SmallIntegerField(choices=limit_choice, default=0, verbose_name="权限")

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Stu(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    sex_choices = (
        ("m", "男"),
        ("f", "女")
    )
    grade = models.IntegerField(verbose_name="年级", null=True)
    major = models.CharField(max_length=255, verbose_name="专业")
    age = models.SmallIntegerField(null=True, verbose_name="年龄")
    sex = models.CharField(choices=sex_choices, max_length=1, default='m', verbose_name="性别")

    # course_table = models.ForeignKey(CourseTable, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Teacher 特有属性
    sex_choices = (
        ("m", "男"),
        ("f", "女")
    )
    sex = models.CharField(choices=sex_choices, max_length=1, default='m', verbose_name="性别")


    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name


class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Admin 特有属性


    class Meta:
        verbose_name = '管理员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


# 学生模型
# username作为id
# class Stu(AbstractUser):
#     sex_choices = [{
#         "m": "男",
#         "f": "女"
#     }]
#     name = models.CharField(max_length=255, verbose_name="姓名")
#     grade = models.IntegerField(verbose_name="年级", null=True)
#     major = models.CharField(max_length=255, verbose_name="专业")
#     phone_number = models.CharField(unique=True, max_length=11, verbose_name="电话号码")
#     age = models.SmallIntegerField(null=True, verbose_name="年龄")
#     sex = models.CharField(choices=sex_choices, max_length=1, default='m', verbose_name="性别")
#     limit = models.SmallIntegerField(default=0, verbose_name="权限")
#     # 因为报错添加
#     groups = models.ManyToManyField(Group, related_name="stu_groups")
#     user_permissions = models.ManyToManyField(Permission, related_name="stu_user_permissions")
#     # course_table = models.ForeignKey(CourseTable, on_delete=models.CASCADE)
#     class Meta:
#         verbose_name = '学生信息'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
#
#
# # 老师模型
# # 用usernam作为工号
# class Teacher(AbstractUser):
#     sex_choices = (
#         ("m", "男"),
#         ("f", "女")
#     )
#     name = models.CharField(max_length=255, verbose_name="姓名")
#     phone_number = models.CharField(unique=True, max_length=11, verbose_name="电话号码")
#     sex = models.CharField(choices=sex_choices, max_length=1, default='m', verbose_name="性别")
#     limit = models.SmallIntegerField(default=1, verbose_name="权限")
#     # 因为报错添加
#     groups = models.ManyToManyField(Group, related_name="teacher_groups")
#     user_permissions = models.ManyToManyField(Permission, related_name="teacher_user_permissions")
#     class Meta:
#         verbose_name = '教师信息'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
#
# class Admin(AbstractUser):
#     name = models.CharField(max_length=10, default="admin", verbose_name="姓名")
#     phone_number = models.CharField(unique=True, max_length=11, verbose_name="电话号码",)
#     limit = models.SmallIntegerField(default=2, verbose_name="权限")
#     # 因为报错添加
#     groups = models.ManyToManyField(Group, related_name="admin_groups")
#     user_permissions = models.ManyToManyField(Permission, related_name="admin_user_permissions")
#     class Meta:
#         verbose_name = '管理员'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name


# class Stu(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=32)
#     password = models.CharField(max_length=64, default="123456")
#     grade = models.CharField(max_length=4)  #
#     major = models.CharField(max_length=20)  #
#     phone_number = models.CharField(max_length=20)  #
#     email = models.EmailField()
#     # 进阶的课程表
#     # course_table = models.CharField(max_length=6, blank=True)
#     age = models.IntegerField(default=20)  #
#     sex = models.CharField(max_length=2)  # 1男,0女


# """
# class StuExtension(models.Model):
#     grade = models.CharField(max_length=4)
#     major = models.CharField(max_length=20)
#     age = models.IntegerField(default=20)
#     sex = models.CharField(max_length=2)  # 1男,0女
#     phone_number = models.CharField(max_length=20)
#     stu = models.OneToOneField("Stu", on_delete=models.CASCADE)
# """


# class Teacher(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=4, default="张三")
#     password = models.CharField(max_length=20, default="123456")
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()
#     sex = models.CharField(max_length=2)
