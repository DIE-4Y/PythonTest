from django.db import models

from user.models import CustomUser


# Create your models here.


class Course(models.Model):
    """课程"""
    name = models.CharField(max_length=10, unique=True, verbose_name='课程名')
    # 注意:teacher是Teacher_id
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="老师")
    # 章节数
    chapter_num = models.IntegerField(verbose_name='章节数')
    credit = models.IntegerField(verbose_name='学分')
    stu_num = models.IntegerField(verbose_name='学生人数')
    course_url = models.URLField(verbose_name='课程网址')
    # 我把他设置为两位数,第一位是周几,第二位是第几节课
    teach_time = models.CharField(max_length=2, verbose_name='上课时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Chapter(models.Model):
    """章节"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    chapter_name = models.IntegerField(verbose_name='章节名称')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.chapter_name

class Video(models.Model):
    """视频资源"""
    name = models.CharField(max_length=20, verbose_name='视频名称')
    video_url = models.URLField(max_length=50, default="https:www.baidu.com", verbose_name='视频网址')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name='第几章')
    upload_file = models.FileField(upload_to='video/', verbose_name='上传视频')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CourseFile(models.Model):
    """课件资源"""
    title = models.CharField(max_length=20, verbose_name='标题')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    uptime = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')
    content = models.TextField(verbose_name='内容')
    chapter = models.CharField(max_length=30, verbose_name='第几章')
    upload_file = models.FileField(upload_to='file', verbose_name='课程资源')

    class Meta:
        verbose_name = '课件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
