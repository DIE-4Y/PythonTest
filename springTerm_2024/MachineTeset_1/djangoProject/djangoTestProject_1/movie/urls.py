from . import views
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

# 指定应用命名空间
app_name = "movie"

urlpatterns = [
    path("",views.index, name="movie_index"),
    path("list/", views.movie_list, name="movie_list"),
    path("detail/<int:movie_id>/", views.movie_details, name="movie_detail")
]
