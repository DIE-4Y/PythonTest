from django.urls import path

from book import views

urlpatterns = [

    path('divide/', views.divide, name='preparation'),
    path('push/', views.push_fun, name='push'),
    path('receive/', views.receive, name='receive'),
    path('bookprocess/', views.book_process, name='book_process'),
    path('articleprocess/', views.article_process, name='article_process'),
    path('pre/',views.pre_process, name='pre_process'),
    path('specified_divide/',views.specified_divide, name='specified_divide'),
    path('textsearch/', views.textsearch, name='textsearch'),
    path('titlesearch/', views.titlesearch, name='titlesearch'),
    path('authorsearch/', views.authorsearch, name='authorsearch'),
    path('get_article/', views.get_article, name='get_article'),
    path('get_book/', views.get_book, name='get_book'),
    # path('upgrade_goal/', views.upgrade_goal, name='upgrade_goal'),
    path('completed_articles/',views.completed_articles,name='completed_articles'),
    path('uncompleted_articles/',views.uncompleted_articles,name='uncompleted_articles'),
    path('check_unpurchased/', views.check_unpurchased, name='check_unpurchased'),
    path('check_purchased/', views.check_purchased, name='check_purchased'),
    path('purchase/', views.purchase, name='purchase'),
    path('switch/', views.switch, name='switch'),
    path('all_book/', views.all_book, name='all_book'),
    path('rerecite/', views.rerecite, name='rerecite'),
    path('review/', views.review, name='review'),
    path('get_book_info/', views.get_book_info, name='get_book_info'),
]
