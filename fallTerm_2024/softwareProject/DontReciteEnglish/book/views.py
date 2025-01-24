import random
import json
from django.http import JsonResponse
from book.models import Article, BookUser, Process, HardSentence, Segment, EasySentence, Book, ArticleUser
from user.models import User

from user.models import User

# Create your views here.
app_name = 'book'


# def upgrade_goal(request):
#     params = json.loads(request.body.decode())
#     user_id = params.get('user_id')
#     goal = params.get('goal')
#     bookuser = BookUser.objects.get(user_id=user_id, status=1)
#     book = bookuser.book
#     book.goal = goal
#     book.save()
#     return JsonResponse({"code": 604, "message": "每日更新量已更新"})


def completed_articles(request):
    params = json.loads(request.body.decode())
    user_id = params.get('user_id')
    bookuser = BookUser.objects.get(user_id=user_id, status=1)
    book = bookuser.book
    articleusers = ArticleUser.objects.filter(book=book, user_id=user_id, difficulty=1)
    articles = []
    for articleuser in articleusers:
        articles.append(articleuser.article)
    # articles = Article.objects.filter(book_id=book.id)
    article_list = [{
        'article_id': article.id,
        'article_title': article.title,
        'article_dynasty': article.dynasty,
        'article_author': article.author,
    } for article in articles]
    data = {
        'article_list': article_list
    }
    return JsonResponse(data)


def uncompleted_articles(request):
    params = json.loads(request.body.decode())
    user_id = params.get('user_id')
    bookuser = BookUser.objects.get(user_id=user_id, status=1)
    book = bookuser.book
    articleusers = ArticleUser.objects.filter(book=book, user_id=user_id, difficulty=0)
    articles = []
    for articleuser in articleusers:
        articles.append(articleuser.article)
    # articles = Article.objects.filter(book_id=book.id)
    article_list = [{
        'article_id': article.id,
        'article_title': article.title,
        'article_dynasty': article.dynasty,
        'article_author': article.author,
    } for article in articles]
    data = {
        'article_list': article_list
    }
    return JsonResponse(data)


def check_unpurchased(request):
    params = json.loads(request.body.decode())
    user_id = params.get('user_id')
    bookusers = BookUser.objects.filter(user_id=user_id, status=0)
    bookuser_list = [{
        'user_id': bookuser.user_id,
        'book_title': bookuser.book.title,
        'book_id': bookuser.book.id,
        'book_avatar': bookuser.book.avatar,
    } for bookuser in bookusers]
    data = {
        'bookuser_list': bookuser_list
    }
    return JsonResponse(data)


def check_purchased(request):
    params = json.loads(request.body.decode())
    user_id = params.get('user_id')
    bookusers = BookUser.objects.filter(user_id=user_id, status__in=[1, 2])
    bookuser_list = [{
        'user_id': bookuser.user_id,
        'book_title': bookuser.book.title,
        'book_id': bookuser.book.id,
        'book_avatar':bookuser.book.avatar,
    } for bookuser in bookusers]
    data = {
        'bookuser_list': bookuser_list
    }
    return JsonResponse(data)


def pre_process(request):
    articles = Article.objects.all()
    for article in articles:
        # text = list(article.text)
        text = article.text
        text = list(filter(lambda x: x != '\n', text))
        text = list(filter(lambda x: x != " ", text))
        # text = list(filter(lambda x: x != '\u3000', text))
        article.text = ''.join(text)
        # article.text = text
        article.save()
    return JsonResponse({"code": 602, "message": "预处理完成"})


def purchase(request):
    params = json.loads(request.body.decode())
    user_id = params.get('user_id')
    book_id = params.get('book_id')
    # user = User.objects.filter(suername=user_id).first()
    book = Book.objects.get(id=book_id)
    try:
        book = Book.objects.get(id=book_id)
        if BookUser.objects.filter(user_id=user_id, status__in=[1, 2], book=book).exists():
            return JsonResponse({"code": 601, "message": "书籍已经被购买过了"})
    except Book.DoesNotExist:
        return JsonResponse({"code": 601, "message": "书籍不存在"})

    user = User.objects.filter(username=user_id).first()
    if user.coin >= book.price:
        bookuser = BookUser.objects.filter(user_id=user_id, book=book).first()
        bookuser.status = 2
        user.coin = user.coin - book.price
        user.save()
        bookuser.save()
        articles = Article.objects.filter(book_id=book_id)
        for article in articles:
            articleuser = ArticleUser(book=book, user_id=user_id, article=article)
            articleuser.save()
        bookuser.save()
        return JsonResponse({"code": 606, "message": "书籍购买成功"})
    else:
        return JsonResponse({"code": 602, "message": "书币不够"})


def switch(request):
    params = json.loads(request.body.decode())
    book_id = params.get('book_id')
    book = Book.objects.get(id=book_id)
    user_id = params.get('user_id')
    bookuser = BookUser.objects.get(user_id=user_id, status=1)
    bookuser.status = 2
    bookuser.save()
    bookuser = BookUser.objects.get(user_id=user_id, book=book)
    if bookuser.status == 0:
        return JsonResponse({"code": 608, "message": "书籍未购买"})
    bookuser.status = 1
    bookuser.save()
    if Process.objects.exists():
        process = Process.objects.get()
        process.delete()
    return JsonResponse({"code": 607, "message": "背诵的书籍更新完毕"})


def specified_divide(request):
    params = json.loads(request.body.decode())
    user_id = params.get('user_id')
    article_id = params.get('article_id')
    article = Article.objects.get(id=article_id)
    articleusers = ArticleUser.objects.filter(article=article, user_id=user_id)
    tf_e = EasySentence.objects.filter(article_id=article_id, user_id=user_id)
    if tf_e.exists():
        return JsonResponse({'code': '609', 'message': "已经得到划分", 'article_id': article_id})
    tf_h = HardSentence.objects.filter(article_id=article_id, user_id=user_id)
    if tf_h.exists():
        return JsonResponse({'code': '609', 'message': "已经得到划分", 'article_id': article_id})
    if HardSentence.objects.filter(article_id=article_id, user_id=user_id) is None:
        return JsonResponse({'code': '999', 'message': "这本书已经背完！"}, status=404)
    text = list(article.text)
    i, j = 0, 0
    for i in range(0, len(text)):
        if text[i] in ['。', '！', '？']:
            sen_text = text[j:i + 1]  # sen_text最后一wei是标点符号
            sentence = HardSentence(text=''.join(sen_text), article_id=article_id, user_id=user_id)
            sentence.save()
            q = j
            for p in range(j, i + 1):
                if text[p] in ['，', '·', '；', '。', '！', '？']:
                    segment_text = text[q:p]
                    segment = Segment(text=''.join(segment_text), sentence=sentence)
                    segment.save()
                    q = p + 1
            j = i + 1
    data = {
        'article_id': article_id
    }
    return JsonResponse(data)


def chose():
    if Article.objects.filter(difficulty=0).exists():
        random_elem = random.choice(Article.objects.filter(difficulty=0))
        return random_elem.id
    else:
        return None


def divide(user_id, book_id):
    articleusers = ArticleUser.objects.filter(user_id=user_id, book_id=book_id, difficulty=0)
    articleuser = random.choice(articleusers)
    article = articleuser.article
    article_id = article.id
    tf_e = EasySentence.objects.filter(article_id=article_id, user_id=user_id)
    if tf_e.exists():
        data = {
            'article_id': article_id
        }
        return data
    tf_h = HardSentence.objects.filter(article_id=article_id, user_id=user_id)
    if tf_h.exists():
        data = {
            'article_id': article_id
        }
        return data
    text = list(article.text)
    i, j = 0, 0
    for i in range(0, len(text)):
        if text[i] in ['。', '！', '？']:
            sen_text = text[j:i + 1]  # sen_text最后一wei是标点符号
            sentence = HardSentence(text=''.join(sen_text), article_id=article_id, user_id=user_id)
            sentence.save()
            q = j
            for p in range(j, i + 1):
                if text[p] in ['，', '·', '；', '。', '！', '？']:
                    segment_text = text[q:p]
                    segment = Segment(text=''.join(segment_text), sentence=sentence)
                    segment.save()
                    q = p + 1
            j = i + 1
    data = {
        'article_id': article_id
    }
    return data


# divide必须和push_fun连用
def push_fun(request):
    params = json.loads(request.body.decode())
    user_id = params.get('user_id')
    book_id = params.get('book_id')
    data = divide(user_id, book_id)
    article_id = data['article_id']
    articleuser = ArticleUser.objects.filter(user_id=user_id, article_id=article_id).first()
    # try:
    #     article_id = params.get('article_id')
    # except :
    #     articleusers = ArticleUser.objects.filter(user_id=user_id,book=book,difficulty=0)
    #     articleuser = random.choice(articleusers)
    #     article = articleuser.article
    #     article_id = article.id
    article = Article.objects.get(id=article_id)
    sentences = HardSentence.objects.filter(article_id=article_id, user_id=user_id)
    if not sentences.exists():
        articleuser.difficulty = 1
        articleuser.save()
        return JsonResponse({"code": 601, "message": "这篇文章已经学完"})
    else:
        # 有 HardSentence 对象
        sentence = random.choice(sentences)
        segments = Segment.objects.filter(sentence=sentence)
        segment = random.choice(segments)
        if Process.objects.exists():
            process = Process.objects.filter().first()
            process.delete()
            # process存储着正在学习的句子
        process = Process(text=sentence.text, article_id=article_id, user_id=user_id)
        process.save()
        seg_text = segment.text
        sen_text = sentence.text
        # tem, tem2 = []
        tem2 = ['_'] * len(seg_text)
        tem3 = ' '.join(tem2)
        tem = sen_text.replace(seg_text, tem3)
        # tem存储替换成'_'的句子文本,tem2是和seg_text同长的字符数组
        data = {
            'article_id': article_id,
            'title': article.title,
            'author': article.author,
            'dynasty': article.dynasty,
            'text': tem,
            'sent_text': sen_text,
            'answer': seg_text,
            'count': sentence.count,
            # 'choice_A':,
            # 'choice_B':,
            # 'choice_C':,
            # 'choice_D':,
            # 'answer':,
        }
        return JsonResponse(data)


def review(request):
    params = json.loads(request.body.decode())
    user_id = params['user_id']
    bookuser = BookUser.objects.filter(user_id=user_id, status=1).first()
    if not bookuser:
        return JsonResponse({"code": 601, "message": "没有找到符合条件的用户或书籍用户"})
    book = bookuser.book

    try:
        process = Process.objects.get(user_id=user_id)
        article_id = process.article_id
    except Process.DoesNotExist:
        articles = Article.objects.filter(book_id=book.id)
        article1 = []
        for article in articles:
            easysentences = EasySentence.objects.filter(article_id=article.id, user_id=user_id)
            for easysentence in easysentences:
                article1.append(easysentence.article_id)
        if not article1:
            return JsonResponse({"code": 601, "message": "目前没有学完的文章"})

        article_id = random.choice(article1)

    easysentences = EasySentence.objects.filter(article_id=article_id, user_id=user_id)
    if not easysentences:
        return JsonResponse({"code": 601, "message": "没有找到相关的简单句子"})

    easysentence = random.choice(easysentences)

    text = list(easysentence.text)
    ran = random.randint(0, len(text) - 1)
    left = ran
    right = ran
    tem = text[ran]
    expand_left = True
    expand_right = True
    while expand_left or expand_right:
        if expand_left:
            if left - 1 < 0 or text[left - 1] in ['，', '·', '；', '。', '！', '？']:
                expand_left = False
            else:
                tem = text[left - 1] + tem
                left -= 1

        if expand_right:
            if right + 1 >= len(text) or text[right + 1] in ['，', '·', '；', '。', '！', '？']:
                expand_right = False
            else:
                tem = tem + text[right + 1]
                right += 1
    tem2 = ['_'] * len(tem)
    tem3 = ' '.join(tem2)
    tem = ' '.join(tem)
    text = ' '.join(text)
    tem4 = text.replace(tem, tem3)
    article = Article.objects.get(id=article_id)

    easylist = {
        'article_id': article_id,
        'title': article.title,
        'author': article.author,
        'dynasty': article.dynasty,
        'text': tem4,
        'answer': tem,
    }
    data = {
        'easylist': easylist
    }
    return JsonResponse(data)


def receive(request):
    params = json.loads(request.body.decode())
    judge = params.get("judge")
    user_id = params.get("user_id")
    process = Process.objects.filter().first()
    article_id = process.article_id
    # article = Article.objects.get(id=article_id)
    sentence = HardSentence.objects.get(text=process.text, article_id=article_id, user_id=user_id)
    user = User.objects.get(username=user_id)
    if judge == "true":
        if sentence.count >= 4:
            sentence.delete()
            new_sentence = EasySentence(text=process.text, article_id=article_id, user_id=user_id)
            new_sentence.save()
            process.delete()
            user.recitation += 1
            user.save()
            return JsonResponse({"code": 602, "message": "这个句子已经学会", 'recitation': user.recitation})
        else:
            sentence.count += 1
            sentence.save()
            process.delete()
            return JsonResponse({"code": 603, "message": "这个句子的背诵情况已更新", 'recitation': user.recitation})
    elif judge == "false":
        if sentence.count > 0:
            sentence.count -= 1
            sentence.save()
            process.delete()
            return JsonResponse({"code": 603, "message": "这个句子的背诵情况已更新", 'recitation': user.recitation})
    else:
        sentence.count = 4
        sentence.delete()
        new_sentence = EasySentence(text=process.text, article_id=article_id, user_id=user_id)
        new_sentence.save()
        process.delete()
    return JsonResponse({"code": 603, "message": "这个句子的背诵情况已更新", 'recitation': user.recitation})


# 这本书内的文章进度
def book_process(request):
    params = json.loads(request.body)
    user_id = params.get("user_id")
    try:
        process = Process.objects.get().first()
        article_id = process.article_id
        article = Article.objects.get(id=article_id).first()
        articleuser = ArticleUser.objects.get(article=article).first()
        book = articleuser.book
    except Process.DoesNotExist:
        bookuser = BookUser.objects.filter(user_id=user_id, status=1).first()
        book = bookuser.book
    hard_article_count = ArticleUser.objects.filter(difficulty=0, book=book, user_id=user_id).count()
    easy_article_count = ArticleUser.objects.filter(difficulty=1, book=book, user_id=user_id).count()
    tem_num = hard_article_count + easy_article_count
    if tem_num == 0:
        data = {
            'rate': 0,
        }
        return JsonResponse(data)
    rate = easy_article_count / tem_num
    data = {
        'rate': rate,
    }
    return JsonResponse(data)


def article_process(request):
    params = json.loads(request.body.decode())
    user_id = params.get("user_id")
    try:
        process = Process.objects.get()
        article_id = process.article_id
    except Process.DoesNotExist:
        return JsonResponse({"code": 601, "msg": "出现内源性错误"})
    hard_sentence_count = HardSentence.objects.all(article_id=article_id, user_id=user_id).count()
    easy_sentence_count = EasySentence.objects.all(article_id=article_id, user_id=user_id).count()
    tem_num = hard_sentence_count + easy_sentence_count
    if tem_num == 0:
        data = {
            'rate': 0,
        }
        return JsonResponse(data)
    rate = easy_sentence_count / tem_num
    data = {
        'rate': rate,
    }
    return JsonResponse(data)


def textsearch(request):
    params = json.loads(request.body.decode())
    content = params.get("content")
    articles = Article.objects.filter(text__contains=content).all()
    articles_list = [
        {'article_id': article.id, 'dynasty': article.dynasty, 'title': article.title, 'author': article.author,
         'text': article.text} for article in articles]
    if len(articles_list) == 0:
        return JsonResponse({"code": 603, "message": "查询文章不存在"})
    data = {
        'articles': articles_list
    }
    return JsonResponse(data)


def authorsearch(request):
    params = json.loads(request.body.decode())
    author = params.get("author")
    articles = Article.objects.filter(author__contains=author).all()
    articles_list = [
        {'article_id': article.id, 'dynasty': article.dynasty, 'title': article.title, 'author': article.author,
         'text': article.text} for article in articles]
    if len(articles_list) == 0:
        return JsonResponse({"code": 603, "message": "查询文章不存在"})
    data = {
        'articles': articles_list
    }
    return JsonResponse(data)


def titlesearch(request):
    params = json.loads(request.body.decode())
    title = params.get("title")
    articles = Article.objects.filter(title__contains=title)
    articles_list = [
        {'article_id': article.id, 'dynasty': article.dynasty, 'title': article.title, 'author': article.author,
         'text': article.text} for article in articles]
    if len(articles_list) == 0:
        return JsonResponse({"code": 603, "message": "查询文章不存在"})
    data = {
        'articles': articles_list
    }
    return JsonResponse(data)


def get_article(request):
    params = json.loads(request.body.decode())
    article_id = params.get("article_id")
    try:
        article = Article.objects.get(id=article_id)
        article_list = [
            {'article_id': article.id, 'dynasty': article.dynasty, 'title': article.title, 'author': article.author,
             'text': article.text}]
        data = {
            'articles': article_list
        }
        return JsonResponse(data)
    except Article.DoesNotExist:
        return JsonResponse({"code": 603, "message": "查询文章不存在"})


# 获取某个书籍包含文章的列表
def get_book(request):
    params = json.loads(request.body.decode())
    user_id = params.get("user_id")
    try:
        book_id = params.get("book_id")
    except:
        return JsonResponse({"code": 605, "message": "书籍不存在"})
    book = Book.objects.get(id=book_id)
    articleusers = ArticleUser.objects.filter(book=book, user_id=user_id)
    articles = []
    for articleuser in articleusers:
        articles.append(articleuser.article)
    article_list = [
        {'article_id': article.id, 'author': article.author, 'dynasty': article.dynasty, 'title': article.title} for
        article in articles]
    data = {
        'articles': article_list
    }
    return JsonResponse(data)


# 展示所有书籍
def all_book(request):
    params = json.loads(request.body.decode())
    user_id = params.get("user_id")
    bookusers = BookUser.objects.filter(user_id=user_id)
    books = []
    for bookuser in bookusers:
        books.append(bookuser.book)
    books_list = [{
        'book_id': book.id,
        'book_title': book.title,
        'status': BookUser.objects.get(user_id=user_id, book=book).status
    } for book in books]
    data = {
        'books': books_list
    }
    return JsonResponse(data)


def get_book_info(request):
    params = json.loads(request.body.decode())
    book_id = params.get("book_id")
    user_id = params.get("user_id")
    book = Book.objects.get(id=book_id)
    books_list = {
        'book_id': book.id,
        'book_title': book.title,
        'book_avatar': book.avatar,
        'book_price': book.price,
        'status': BookUser.objects.get(user_id=user_id, book=book).status
    }
    data = {
        'books': books_list
    }
    return JsonResponse(data)


def rerecite(request):
    params = json.loads(request.body.decode())
    user_id = params.get("user_id")
    article_id = params.get("article_id")
    easysentences = EasySentence.objects.filter(article_id=article_id, user_id=user_id)
    hardsentences = HardSentence.objects.filter(article_id=article_id, user_id=user_id)
    for hardsentence in hardsentences:
        hardsentence.count = 0
        hardsentence.save()
    return JsonResponse({"code": 605, "message": "已重置背诵进度"})
    for easysentence in easysentences:
        text = easysentence.text
        easysentence.delete()
        hardsentence = HardSentence(article_id=article_id, user_id=user_id, text=text)
        hardsentence.save()
    return JsonResponse({"code": 605, "message": "已重置背诵进度"})
