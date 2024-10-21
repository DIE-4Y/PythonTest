from django.contrib import admin

from course.models import Course, Video, CourseFile, Chapter
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'chapter_num', 'credit', 'stu_num',
                    'course_url', 'teach_time']
    search_fields = ['name', 'teacher', 'chapter_num', 'credit', 'teach_time',]

class ChapterAdmin(admin.ModelAdmin):
    list_display = ['course', 'chapter_name']
    search_fields = ['course', 'chapter_name']

class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'video_url', 'chapter', 'upload_file']
    search_fields = ['name', 'chapter']
class CourseFileAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'uptime', 'content', 'chapter', "upload_file"]
    search_fields = ['title', 'course', 'chapter']


# admin后台注册
admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(CourseFile,CourseFileAdmin)
