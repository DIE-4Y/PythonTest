from django.db import models
from study.models import Course

# Create your models here.

class Gender(models.Model):
    GENDER_CHOICE=(
        ("M", "男"),
        ("F", "女"),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)

# 学生表
class Student(models.Model):
    stu_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    academy = models.CharField(max_length=20)
    major = models.CharField(max_length=20)

# 老师表
class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField(default= 30)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    course = models.ManyToManyField(Course, related_name="teachers")

# 管理员
class admin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

