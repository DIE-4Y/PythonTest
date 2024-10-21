from django.db import models

from course.models import Course
from user.models import Stu, CustomUser


# Create your models here.

# 考试,测验
# 课程,章节,是考试/测验,学生,这四个属性唯一确定一个exam
class Exam(models.Model):
    name = models.CharField(max_length=10, verbose_name="考试名称")
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams', verbose_name="课程")
    chapter = models.IntegerField(default=0, verbose_name="章节数")
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="exams", verbose_name="考试学生")
    question_num = models.IntegerField(default=0,verbose_name="题目数")
    # start_datetime = models.DateTimeField(verbose_name="开始时间")
    # end_datetime = models.DateTimeField(verbose_name="结束时间")
    time_long = models.IntegerField(default=0, verbose_name="考试时长")

    # 判断是考试还是测验,测验就将成绩存在ExamScore中,考试就存在Course_student中,默认是考试
    # is_exam = models.BooleanField(default=True, verbose_name="考试类型")

    class Meta:
        verbose_name = '考试'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 单选题
class Choice(models.Model):
    label = models.IntegerField(default=1, verbose_name="题型")
    answer_choices = (
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    )
    content = models.CharField(max_length=100, verbose_name="题目")
    A_CHOICES = models.CharField(max_length=255, verbose_name="A选项")
    B_CHOICES = models.CharField(max_length=255, verbose_name="B选项")
    C_CHOICES = models.CharField(max_length=255, verbose_name="C选项")
    D_CHOICES = models.CharField(max_length=255, verbose_name="D选项")
    answer = models.CharField(max_length=1, choices=answer_choices, verbose_name="答案")
    weight = models.IntegerField(verbose_name="分值")
    chapter = models.CharField(max_length=30, verbose_name="章节")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='choices', verbose_name="考试")

    class Meta:
        verbose_name = '单选题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


# 填空题
class BlankFilling(models.Model):
    label = models.IntegerField(default=2, verbose_name="题型")
    content = models.CharField(max_length=100, verbose_name="题目")
    weight = models.IntegerField(verbose_name="分值")
    answer = models.CharField(max_length=100, verbose_name="答案")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='blankFillings', verbose_name="考试")

    class Meta:
        verbose_name = '填空题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


# 主观题
class Subjective(models.Model):
    label = models.IntegerField(default=3, verbose_name="题型")
    content = models.CharField(max_length=100, verbose_name="题目")
    weight = models.IntegerField(verbose_name="分值")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='subjectives', verbose_name="考试")

    class Meta:
        verbose_name = '主观题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


# 主观题作答情况
class SubAnswer(models.Model):
    answer = models.CharField(max_length=250, verbose_name="作答", null=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subjective = models.ForeignKey(Subjective, on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name="得分", default=-1)

    class Meta:
        verbose_name = '主观题作答'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.answer


# 选择题作答情况
class ChoiceAnswer(models.Model):
    answer = models.CharField(max_length=250, verbose_name="作答")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='ChoiceAnswers', verbose_name="选择题作答")
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='ChoiceAnswers')
    score = models.IntegerField(verbose_name="得分", default=0)

    class Meta:
        verbose_name = '选择题作答'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.answer


# 填空题作答情况
class BFAnswer(models.Model):
    answer = models.CharField(max_length=250, verbose_name="作答")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='BFAnswers', verbose_name="填空题作答")
    blankfilling = models.ForeignKey(BlankFilling, on_delete=models.CASCADE, related_name='BFAnswers')
    score = models.IntegerField(verbose_name="得分", default=0)

    class Meta:
        verbose_name = '填空题作答'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.answer


# 测验成绩记录
class ExamScore(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name="测验成绩", default=-1)
