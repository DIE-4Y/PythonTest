from django.db import models
from django.core import validators

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.SmallIntegerField()
    email = models.EmailField()

    # 数据库中重命名
    class Meta:
        db_table = "front_author"

class Publisher(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "front_publisher"

class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.SmallIntegerField()
    price = models.FloatField()
    rating = models.FloatField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        db_table="front_book"

class BookOrder(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.FloatField()

    class Meta:
        db_table="front_book_oder"

# modleForm继承创建的模型部分
class Article(models.Model):
    title = models.CharField(max_length=200, validators=[validators.MinLengthValidator(limit_value=2)])
    content = models.TextField(validators=[validators.MinLengthValidator(limit_value=3)])
    # 指定了auto_now_add表单中不用传入这个字段
    creat_time = models.DateTimeField(auto_now_add=True)
    # 如果给了blank=True那么表单验证中可以为空,可传可不传
    # 但是存入数据库不能为空
    category = models.CharField(max_length=20, blank=True)