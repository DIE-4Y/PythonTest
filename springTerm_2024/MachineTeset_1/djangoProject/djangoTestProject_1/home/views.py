from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def index(request):
    return render(request, "home_index.html")

# html变量读取用context字典传递
def inform(request):
    # 1.变量
    selfintroduction = "我是Assinal"
    # 2.字典
    book = {"id": 1, "name": "ThreeBody", "author": "LiuCixin"}
    # 3.数组
    books = [
        {"id": 1, "name": "三体", "author": "刘慈欣"},
        {"id": 2, "name": "西游记", "author": "吴承恩"}
    ]
    # 4.对象
    class Person:
        def __init__(self,realname):
            self.realname = realname

    context={"selfintroduction":selfintroduction,
             "book":book,
             "books":books,
             "person":Person("Assianl")}
    return render(request, "inform.html", context=context)


# 标签使用
# if标签
def if_view(request):
    money = 6000
    return render(request, "if.html", context={"money": money})

# for...in...标签empty处理
# 反向遍历reverse,计数器forloop.counter1/0,

def for_view(request):
    # 1.列表
    books = [{"name":"西游记","author":"吴承恩"},
              {"name":"水浒传","author":"施耐庵"},
             {"name":"三国演义","author":"罗贯中"},
             {"name":"红楼梦","author":"曹雪芹"}]
    # 2.字典
    # for X in person.items, values, keys三种遍历方式
    person = {
        "name":"Assinal",
        "age":20,
        "sex":"男",
        "QQ":"239597838",
    }
    context = {"books":books,"person":person}
    return render(request, "for.html", context=context)


# with标签命名常用变量
def with_view(reqeust):
    books = [
        {"name": "西游记", "author": "吴承恩"},
        {"name": "水浒传", "author": "施耐庵"},
        {"name": "三国演义", "author": "罗贯中"},
        {"name": "红楼梦", "author": "曹雪芹"}
    ]

    context={"books":books}
    return render(reqeust, "with.html", context = context)


# url翻转（类似路由反转）有app命要appName:name
def url_view(request):
    return render(request, "url.html")

# filter使用add,cut,
def filter_view(request):
    # cut过滤器
    greet = "words Hello World, I am Assinal"
    # time过滤器
    time = datetime.now()
    # default标签
    introduction = ""
    # safe过滤器,识别html标签
    html = "<h3>这是一个safe标签</h3>"
    context={"greet": greet, "time": time,"introduction": introduction, "html": html}
    return render(request, "filter.html", context=context)

# include标签实现html文件,文件里的变量也可使用,可放在任何地方
# extends标签继承html文件,必须放在html第一行
def template_form(request):
    news={"article1": "小米su7发布", "article2": "Chat GPT5发布"}
    context={"news":news}
    return render(request, "cp.html", context=context)
