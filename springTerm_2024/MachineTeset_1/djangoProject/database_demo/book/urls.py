from django.urls import path
from . import views

app_name = "book"


urlpatterns =[
    path("add/", views.book_add, name = "book_add"),
    path("query/", views.book_query, name="book_query"),
    path("sort/", views.book_sort, name="book_sort"),
    path("update/", views.book_update, name="book_update"),
    path("delete/", views.book_delete, name="book_delete"),
]