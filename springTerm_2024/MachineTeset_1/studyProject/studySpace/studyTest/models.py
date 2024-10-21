from django.db import models
from user.models import Teacher, Student
from study.models import Chapter, Course
# Create your models here.


class Examination(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    question = models.ManyToManyField("Question", related_name="examinations")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Question(models.Model):
    # 题型
    TAG_CHOICE = (
        ("SingleChoice", "单选题"),
        ("MultipleChoice", "多选题"),
        ("Judge", "判断题"),
        ("ShortAnswer", "简答题"),
        ("Vocabulary", "应用题")
    )

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    content = models.TextField()
    answer = models.TextField()
    tag = models.CharField(max_length=14, choices=TAG_CHOICE)
    weight = models.SmallIntegerField(default=0) # 分值
    examination = models.ManyToManyField(Examination, related_name="questions")

class Score(models.Model):
    score = models.SmallIntegerField(default=0)
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
