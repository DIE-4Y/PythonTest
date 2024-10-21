from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("欢迎来到movie应用")

def movie_list(request):
    return HttpResponse("电影列表")

def movie_details(request, movie_id):
    return HttpResponse("您查找的电影id是：{}".format(movie_id))
