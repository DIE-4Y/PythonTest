from django.db import models

# 外键的运用
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20, default="123456")

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    # 引入外键
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    tag = models.ForeignKey("Tag", on_delete=models.DO_NOTHING, related_name="articles", null=True)

class Tag(models.Model):
    name = models.CharField(max_length=20, default=None)

class Comment(models.Model):
    words = models.TextField()
    article = models.ForeignKey("article.Article", on_delete=models.CASCADE, default=None)

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)

class Teacher(models.Model):
    name = models.CharField(max_length=20)

class Admin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
