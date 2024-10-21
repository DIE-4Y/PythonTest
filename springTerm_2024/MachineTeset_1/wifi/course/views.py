import random
import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from course.models import Course, CourseFile, Chapter, Video
from user.models import CustomUser


# Create your views here.

# 管理员添加课程
# @require_http_methods(["POST", "GET"])
# @login_required
def add_course(request):
    """添加课程"""
    params = json.loads(request.body.decode())
    course_name = params['course_name']
    teacher_username = params.get("teacher_username")
    teacher = CustomUser.objects.get(username=teacher_username)
    chapter_num = params.get("chapter_num")
    credit = params.get("credit")
    stu_num = params.get("stu_num")
    course_url = params.get("course_url")
    teach_time = params.get("teach_time")
    Course.objects.update_or_create(name=course_name, teacher=teacher, chapter_num=chapter_num, credit=credit,
                                    stu_num=stu_num, course_url=course_url, teach_time=teach_time)
    return JsonResponse({"code": "200", "message": "课程创建成功"})


# @login_required
def add_chapter(request):
    """创建章节"""
    params = json.loads(request.body.decode())
    course_name = params.get("course_name")
    chapter_name = params.get("chapter_name")
    if not course_name or not chapter_name:
        return JsonResponse({"code": "400", "message": "参数缺失"})
    if not Course.objects.filter(name=course_name).exists():
        return JsonResponse({"code": "400", "message": "未找到该课程"})
    course = Course.objects.filter(name=course_name).first()
    Chapter.objects.create(course=course, chapter_name=chapter_name)
    return JsonResponse({"code": "200", "message": "创建章节成功"})


def add_course_file(request):
    """添加课程文件"""
    params = json.loads(request.body.decode())
    title = params.get('title')
    course_name = params.get('course_name')
    content = params.get('content')
    chapter = params.get('chapter')
    # upload_file = request.FILES.get('upload_file')
    """暂时不添加课程文件，因为无法测试"""
    # if not title or not course_name or not content or not chapter or not upload_file:
    #     return JsonResponse({"code": "400", "message": "参数缺失"})

    if not title or not course_name or not content or not chapter:
        return JsonResponse({"code": "400", "message": "参数缺失"})

    try:
        course = Course.objects.get(name=course_name)
    except Course.DoesNotExist:
        return JsonResponse({"code": "400", "message": "未找到该课程"})

    CourseFile.objects.create(
        title=title,
        course=course,
        content=content,
        chapter=chapter,
        # upload_file=upload_file
    )

    return JsonResponse({"code": "200", "message": "课程文件创建成功"})


def add_video_file(request):
    """添视频"""
    params = json.loads(request.body.decode())
    course_name = params.get('course_name')
    chapter_name = params.get('chapter_name')
    name = params.get('name')
    video_url = params.get('video_url')
    # upload_file = request.FILES.get('upload_file')
    """暂时不添加视频文件，因为无法测试"""
    # if not course_name or not chapter_name or not name or not video_url or not upload_file:
    if not course_name or not chapter_name or not name or not video_url:
        return JsonResponse({'code': '400', 'message': '参数缺失'})

    if Course.objects.filter(name=course_name).exists():
        course = Course.objects.filter(name=course_name).first()
        if Chapter.objects.filter(course=course, chapter_name=chapter_name).exists():
            chapter = Chapter.objects.filter(course=course, chapter_name=chapter_name).first()
            Video.objects.create(name=name, video_url=video_url, chapter=chapter)
            # Video.objects.create(name=name, video_url=video_url, chapter=chapter, upload_file=upload_file)
            return JsonResponse({'code': '200', 'message': '视频添加成功'})
        else:
            return JsonResponse({'code': '400', 'message': '没有改名称的章节'})
    else:
        return JsonResponse({'code': '400', 'message': '没有该名称的课程'})


"""
def create_video(request):
    name =     models.CharField(max_length=10)
    video_url =     models.URLField(max_length=50, default="https:www.baidu.com")
    course =       models.ForeignKey("Course", on_delete=models.CASCADE)
    chapter =     models.CharField(max_length=10)
"""
