from django.urls import path
from course import views

app_name = 'course'

urlpatterns = [
    path("addcourse/", views.add_course, name="addcourse"),
    path("addchapter/", views.add_chapter, name="addchapter"),
    path('addcoursefile/', views.add_course_file, name="createcoursefile"),
    path('addvideofile/', views.add_video_file, name="createvideofile"),
]