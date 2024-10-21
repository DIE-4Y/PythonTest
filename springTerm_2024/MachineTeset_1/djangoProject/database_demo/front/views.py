from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg, Count, Max, Min, Sum, F, Q
from .models import Book, BookOrder, Publisher, Author
from .forms import MessageBoardForm, RegisterForm, ArticleForm
# 请求验证装饰器
from django.views.decorators.http import require_http_methods
# Create your views here.

# 使用聚合函数:aggregate
# 平均之计算函数:Avg

def avg_view(request):
    result = Book.objects.aggregate(my_avg=Avg("price"))
    print(result)
    return HttpResponse("平均价格计算完毕!")

# 技术函数:Count
def count_view(request):
    result = Book.objects.aggregate(book_count=Count("id"))
    print(result)
    return HttpResponse("书本总数计算完毕！")

# 最大最小函数:Max, Min
def max_min_view(request):
    ma = Author.objects.aggregate(Max("age"))
    mi = Author.objects.aggregate(Min("age"))
    print(ma)
    print(mi)
    return HttpResponse("年龄查找完毕")

# 指定求和函数:Sum
# bookorder__XXX是从bookoder中找与book有关的全部进行对应计算
# aggregate只简单返回字段的值
# annotate会自动用主键分组返回一个字典类型,它的值可以用.values指定
def sum_view(request):
    result = Book.objects.annotate(total=Sum("bookorder__price")).values("name", "total")
    print(result)
    return HttpResponse("总销售额计算完毕")


# F表达式,在sql语句生成时动态返回F表达式的值
def f_view(request):
    Book.objects.update(price=F("price")-10)
    return HttpResponse("全部书籍价格降低10元！")

# Q表达式,可处理逻辑与'&'或'|'非'~'问题
def q_view(request):
    books = Book.objects.filter(Q(price__gte=86) | Q(rating__gte=9)).all()
    for book in books:
        print(book.name, book.price)
    return HttpResponse("处理完毕！")

# form表单
# GET请求：一般从服务器获取数据,访问网址默认用GET
# POST请求：一般向服务器提交数据
# 其他请求PUT/DELETE/HEAD
# 1.渲染页面，

@require_http_methods(["GET","POST"])
# 现在网页只能用GET或POST请求


# 暂时需要把settings里的'django.middleware.csrf.CsrfViewMiddleware',注释才囊运行

def form_view(request):
    # 用GET请求直接诶返回一个网页
    if request.method == "GET":
        form = MessageBoardForm()
        context= {"form": form}
        return render(request, "form_index.html", context=context)
    # 用POST提交的数据验证是否满足要求
    elif request.method == "POST":
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            email = form.cleaned_data["email"]
            return HttpResponse("{}{}{}".format(title, content, email))
        else:
            print("form error")
            return HttpResponse("表单验证失败！")

# 验证器验证表单
@require_http_methods(["GET","POST"])
def register_view(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data["telephone"]
            return HttpResponse(telephone)
        else:
            print(form.errors.get_json_data())
            return HttpResponse("表单验证失败")

@require_http_methods(["GET", "POST"])
def article_view(request):
    if request.method == "GET":
        return render(request, "article.html")
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 获取title,content,creat_time,创建article模型,存储到数据库中
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            creat_time=form.cleaned_data.get("creat_time")
            return HttpResponse("{}{}{}".format(title,content,creat_time))
        else:
            print(form.errors.get_json_data())
            return HttpResponse("表单验证失败！")
