from django.db import models

from course.models import Course
from user.models import CustomUser


# Create your models here.
class Course_student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="学生")
    score = models.IntegerField(default=-1, verbose_name="课程成绩")

    class Meta:
        verbose_name = "学生课程表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.course} - {self.student} - 分数: {self.score}"

