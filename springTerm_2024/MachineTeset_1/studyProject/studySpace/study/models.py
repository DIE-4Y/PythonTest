from django.db import models


# Create your models here.

# 章节
class Chapter(models.Model):
    name = models.CharField(max_length=20)
# 视频
class Video(models.Model):
    name = models.CharField(max_length=20)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    description = models.TextField()
    upload_time = models.DateTimeField(auto_now_add=True)
    origin_url = models.URLField()

# 课程
class Course(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True)
    course_name = models.CharField(max_length=20, unique=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    videos = models.ForeignKey(Video, on_delete=models.CASCADE)
