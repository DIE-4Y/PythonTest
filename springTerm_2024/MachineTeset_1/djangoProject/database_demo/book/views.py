from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import Book

# Create your views here.


# 向数据库新增数据
def book_add(request):
    # book = Book(name="三国演义", author="罗贯中", price=30)
    # book = Book(name="水浒传",author="施耐庵", price=128)
    # book = Book(name= "西游记", author="吴承恩", price=77)
    book = Book(name="红楼梦", author="曹雪芹", price= 89)
    book.save()
    return HttpResponse("书籍加入成功！")

# 查找数据库的数据
def book_query(reqeust):
    # 查找所有
    # books = Book.objects.all()
    # 过滤查找
    books = Book.objects.filter(author="罗贯中")
    for book in books:
        print(book.name)
    return HttpResponse("书籍查找成功！")


# 排序order_by,如果想倒序就加一个‘-’
def book_sort(reqeust):
    books = Book.objects.order_by("-price")
    for book in books:
        print(book.name)
    return HttpResponse("书籍排序完成！")

# 查找一条记录并修改数据
def book_update(request):
    book = Book.objects.get(author="罗贯中")
    book.name="Journey To The West"
    book.save()
    return HttpResponse("书籍修改成功")

# 查找并一条记录删除, 删除不用保存
def book_delete(request):
    book = Book.objects.get(name="红楼梦")
    book.delete()
    return HttpResponse("书籍删除成功")