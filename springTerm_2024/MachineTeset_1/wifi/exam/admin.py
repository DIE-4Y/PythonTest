from django.contrib import admin
from .models import Course, Choice, BlankFilling, Subjective, Exam, SubAnswer, ChoiceAnswer, BFAnswer


# Register your models here.

class ExamAdmin(admin.ModelAdmin):
    list_display = ["name", "pub_time", "time_long","question_num"]
    search_fields = ["name", "pub_time",  "time_long""question_num"]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["content", "A_CHOICES", "B_CHOICES", "C_CHOICES",
                    "D_CHOICES", "answer", "weight", "chapter", "exam"]
    search_fields = ["content", "A_CHOICES", "B_CHOICES", "C_CHOICES",
                    "D_CHOICES", "answer", "weight", "course", "chapter", "exam"]


class BlankFillingAdmin(admin.ModelAdmin):
    list_display = ["content", "weight", "answer", "exam"]
    search_fields = ["content", "weight", "exam"]

class SubjectiveAdmin(admin.ModelAdmin):
    list_display = ["content", "weight", "exam",]
    search_fields = ["content", "weight", "exam"]

class SubAnswerAdmin(admin.ModelAdmin):
    list_display = ["answer", "exam", "subjective", "score"]
    search_fields = ["answer", "exam", "subjective", "score"]

class ChoiceAnswerAdmin(admin.ModelAdmin):
    list_display = ["answer", "exam", "choice", "score"]
    search_fields = ["answer", "exam", "choice", "score"]

class BFAnswerAdmin(admin.ModelAdmin):
    list_display = ["answer", "exam", "blankfilling", "score"]
    search_fields = ["answer", "exam", "blankfilling", "score"]


admin.site.register(Choice, ChoiceAdmin)
admin.site.register(BlankFilling, BlankFillingAdmin)
admin.site.register(Subjective, SubjectiveAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(SubAnswer, SubAnswerAdmin)
admin.site.register(ChoiceAnswer, ChoiceAnswerAdmin)
admin.site.register(BFAnswer, BFAnswerAdmin)