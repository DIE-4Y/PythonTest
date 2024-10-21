from . import views
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

app_name = "home"

urlpatterns = [
    path("index/", views.index, name="home_index"),
    path("inform/", views.inform, name="inform"),
    path("if/", views.if_view, name="if"),
    path("for/", views.for_view, name="for"),
    path("with/", views.with_view, name="with_view"),
    path("url/", views.url_view, name="url_view"),
    path("filter/", views.filter_view, name="filter_view"),
    path("template/", views.template_form, name="template_form"),
]
