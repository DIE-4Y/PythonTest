from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# URL中携带参数包括两种情况
# 1.关键字是参数
# 2.路径中有参数

# 关键字查询 http://127.0.0.1:8000/book/?id=1&name=三国志
def book_detail_query_string(request):
    # request传入的是字典 {"id":1, "name":"三国志"}
    book_id = request.GET.get("id")
    book_name = request.GET.get("name")
    return HttpResponse("您查找的书本id是:{}；名称是:{}".format(book_id, book_name))

# 路径查询 http://127.0.0.1:8000/book/1
# 路径为str类型
def book_query_path_str(request, book_id):
    return HttpResponse("您查找的书本id是：{}".format(book_id))

# 路径为int类型
def book_query_path_int(request, book_id):
    return HttpResponse("您查找的书本id是：{}".format(book_id))

# 路径为slug类型
def book_query_path_slug(request, book_id):
    return HttpResponse("您查找的书本id是：{}".format(book_id))

# 路径为path类型
def book_query_path_path(request, book_id):
    return HttpResponse("您查找的书本id是：{}".format(book_id))

