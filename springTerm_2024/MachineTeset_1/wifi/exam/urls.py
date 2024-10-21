from django.urls import path

from . import views

app_name = 'exam'

urlpatterns = [
    # path('get_exam/', views.get_exam_id, name="get_exam"),
    path('get_exams/', views.get_exams, name="get_exams"),
    path('get_exam_more/', views.get_exam_more, name="get_exam_more"),
    # path('getquestion/', views.get_questions, name="get_questions"),
    path('save_answer/', views.save_answer, name="save_answer"),
    path('get_subjective/', views.get_subjective, name="get_subjective"),
    path('update_subanswer_scores/', views.update_subanswer_scores, name="update_subanswer_scores"),
    # path('', views.judge_bfanswer, name="judge_bfanswer"),
    # path('', views.judge_choiceanswer, name="judge_choiceanswer"),
    path('calculate_exam_total_score/', views.calculate_exam_total_score, name="calculate_exam_total_score"),
    # path('get_exam_answers/', views.get_exam_answers, name="get_exam_answers"),
]
