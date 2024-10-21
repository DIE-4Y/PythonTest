from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, User, Tag
def text_view(request):
    # users = User(username="Assinal", password="root")
    # users.save()
    # articles = Article(title="Django学习", content="现在在学习数据库有关内容", author=users)
    # articles.save()
    article = Article.objects.first()
    return HttpResponse(article.author.username)

def tagadd_view(request):
    tag = Tag(name="学习")
    tag.save()
    article = Article.objects.first()
    article.tag = tag
    article.save()
    return HttpResponse("tag加入成功:",tag.name)