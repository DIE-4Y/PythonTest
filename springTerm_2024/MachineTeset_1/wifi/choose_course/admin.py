from django.contrib import admin

from .models import  Course_student


class Course_studentAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'score')
    search_fields = ('course', 'student', 'score')


admin.site.register(Course_student, Course_studentAdmin)
