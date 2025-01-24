import os

from django.db import models


from django.conf import settings

from user.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, default="唐诗宋词四十首")  # 书籍名
    avatar = models.CharField(max_length=666,null=True)
    price = models.IntegerField(default=100)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title


class BookUser(models.Model):
    user_id = models.CharField(max_length=20)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # 0代表未获取,1代表在背,2代表目前不在背诵
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'BookUser'


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=10)
    dynasty = models.CharField(max_length=10)
    text = models.TextField()  # 原文
    book_id = models.IntegerField()

    # translations = models.CharField(max_length=1000)  # 译文

    class Meta:
        db_table = 'Article'

    def __str__(self):
        return self.title


class ArticleUser(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 0是不会,1是已经学会
    difficulty = models.IntegerField(default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=20)

    class Meta:
        db_table = 'ArticleUser'


# class EasyList(models.Model):
#     ar = models.ForeignKey(Book, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'easylist'
#
#
# class HardList(models.Model):
#     article_id = models.IntegerField()
#
#
#     class Meta:
#         db_table = 'hardlist'ticle_id = models.IntegerField()
#     book


class EasySentence(models.Model):
    text = models.CharField(max_length=200)
    article_id = models.IntegerField()
    user_id = models.CharField(max_length=20)

    class Meta:
        db_table = 'easysentence'


class HardSentence(models.Model):
    text = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    article_id = models.IntegerField()
    user_id = models.CharField(max_length=20)

    class Meta:
        db_table = 'hardsentence'


class Segment(models.Model):
    text = models.CharField(max_length=200)
    sentence = models.ForeignKey(HardSentence, on_delete=models.CASCADE)
    class Meta:
        db_table = 'segment'


# 待排序的
class Process(models.Model):
    text = models.CharField(max_length=200)
    article_id = models.IntegerField()
    user_id = models.CharField(max_length=20)

    class Meta:
        db_table = 'process'
