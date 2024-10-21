from django.urls import path
from . import views


app_name = "article"

urlpatterns = [
    path("test/",views.text_view, name="text_view"),
   # path("tagadd/", views.tagadd_view, name="tagadd_view"),
]