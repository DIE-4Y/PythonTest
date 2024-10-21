import json

from django.db.models import Sum
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from choose_course.models import Course_student
from course.models import Course
from exam.models import BlankFilling, Choice, Subjective, Exam, SubAnswer, ChoiceAnswer, BFAnswer, ExamScore
from user.models import CustomUser


# Create your views here.

# # 上传exam_id
# def get_exam_id(request):
#     params = json.loads(request.body)
#     course_name = params.get('course_name')
#     course = Course.objects.get(name=course_name)
#     chapter = params.get('chapter')
#     student_id = params.get('student_id')
#     student = CustomUser.objects.get(username=student_id)
#     is_exam = params.get('is_exam')
#     # if Exam.objects.filter(course=course, student=student).exists():
#     #     exam = Exam.objects.get(is_exam=is_exam, course=course, chapter=chapter,
#     #                         student=student)
#     #     return JsonResponse({"exam_id": exam.id})
#     # else:
#     #     return JsonResponse({"code": 400, "message": "找不到该次考试"})
#
#     if Exam.objects.filter(is_exam=is_exam, course=course, chapter=chapter).exists():
#         exam = Exam.objects.get(is_exam=is_exam, course=course, chapter=chapter)
#
#     exams = Exam.objects.get(is_exam=is_exam, course=course, chapter=chapter)
#     if exams is None:
#         return JsonResponse({"code": 400, "message": "找不到考试信息1"})
#     for exam in exams:
#         if student in exam.student.all():
#             # 如果找到了匹配的考试并且学生参加了该考试
#             return JsonResponse({"exam_id": exam.id})
#     return JsonResponse({"code": 400, "message": "找不到考试信息2"})


def get_exams(request):
    params = json.loads(request.body)
    course_name = params.get('course_name')
    try:
        course = Course.objects.get(name=course_name)
    except Course.DoesNotExist:
        return JsonResponse({"status": "error", "message": "课程不存在"}, status=400)
    exams = Exam.objects.filter(course=course)
    exam1 = []
    for exam in exams:
        exam1.append(exam.id)
    data = {"data": exam1}
    return JsonResponse(data)


def get_exam_more(request):
    params = json.loads(request.body)
    exam_id = params.get('exam_id')
    exam = Exam.objects.get(id=exam_id)
    try:
        examscores = ExamScore.objects.filter(exam=exam)
        examscore = examscores.last()
    # 如果没做过这套题
    except ExamScore.DoesNotExist:
        StateCode = 0
        timelong = exam.time_long
        question_num = exam.question_num
        test = [StateCode, timelong, question_num]
        choices = Choice.objects.filter(exam=exam)
        for choice in choices:
            select = [choice.A_CHOICES, choice.B_CHOICES, choice.C_CHOICES, choice.D_CHOICES]
            data = {"select": select, "tag": 1, "question": choice.content, "weight": choice.weight}
            test.append(data)
        blankfillings = BlankFilling.objects.filter(exam=exam)
        for blankfilling in blankfillings:
            data = {"select": None, "tag": 2, "question": blankfilling.content, "weight": blankfilling.weight}
            test.append(data)
        subjectives = Subjective.objects.filter(exam=exam)
        for subjective in subjectives:
            data = {"select": None, "tag": 3, "question": subjective.content, "weight": subjective.weight}
            test.append(data)
        data = {"data": test}
        return JsonResponse(data)
    # 如果做过这套题
    StateCode = 1
    test = [StateCode]
    for choice in Choice.objects.filter(exam=exam):
        select = [choice.A_CHOICES, choice.B_CHOICES, choice.C_CHOICES, choice.D_CHOICES]
        question = choice.content
        score = choice.weight
        choice_answer = ChoiceAnswer.objects.get(choice=choice, exam=exam)
        stuanswer = choice_answer.answer
        answer = choice.answer
        data = {"tag": 1, "question": question, "score": score, "select": select, "answer": answer,
                "stuanswer": stuanswer}
        test.append(data)
    for blankfilling in BlankFilling.objects.filter(exam=exam):
        question = blankfilling.content
        score = blankfilling.weight
        blankfilling_answer = BFAnswer.objects.get(blankfilling=blankfilling, exam=exam)
        stuanswer = blankfilling_answer.answer
        answer = blankfilling.answer
        data = {"tag": 2, "question": question, "score": score, "select": None, "answer": answer,
                "stuanswer": stuanswer}
        test.append(data)
    for sub in Subjective.objects.filter(exam=exam):
        question = sub.content
        score = sub.weight
        sub_answer = SubAnswer.objects.get(subjective=sub, exam=exam)
        stuanswer = sub_answer.answer
        data = {"tag": 2, "question": question, "score": score, "select": None, "answer": None,
                "stuanswer": stuanswer}
        test.append(data)
    data = {"data": test}
    return JsonResponse(data)


# # 上传题目
# def get_questions(request):
#     # 获取exam对象
#     params = json.loads(request.body)
#     exam_id = params.get('exam_id')
#     exam = Exam.objects.get(id=exam_id)
#
#     # 假设Choice、BlankFilling和Subjective模型都有一个指向Exam的外键
#     # 使用Prefetch_related进行预加载，以减少数据库查询次数
#     questions = {
#         'choices': Choice.objects.filter(exam=exam).select_related('exam').prefetch_related('...'),
#         # 如果Choice有其他外键关系，也可以在这里预加载
#         'blankfillings': BlankFilling.objects.filter(exam=exam).select_related('exam').prefetch_related('...'),
#         'subjectives': Subjective.objects.filter(exam=exam).select_related('exam').prefetch_related('...'),
#     }
#     # 将Django ORM查询集序列化为Python字典列表
#     serialized_questions = {
#         'choices': list(questions['choices'].values()),
#         'blankfillings': list(questions['blankfillings'].values()),
#         'subjectives': list(questions['subjectives'].values()),
#     }
#     # 返回JSONResponse
#     return JsonResponse(serialized_questions)


# 接收并记分选择,填空,主观作答
def save_answer(request):
    global score
    params = json.loads(request.body.decode())
    exam_id = params.get('exam_id')
    exam = Exam.objects.get(id=exam_id)
    answers = params.get('answer')
    choices = Choice.objects.filter(exam=exam)
    blankfillings = BlankFilling.objects.filter(exam=exam)
    subjectives = Subjective.objects.filter(exam=exam)
    if 1 in answers:
        for choice, value in zip(choices, answers[1]):
            answer = answers[1][value]
            if answer == choice.answer:
                score = choice.weight
            else:
                score = 0
            choiceanswer = ChoiceAnswer(exam=exam, choice=choice, answer=answer, score=score)
            choiceanswer.save()
    if 2 in answers:
        for blankfilling, value in zip(blankfillings, answers[2]):
            answer = answers[2][value]
            if answer == blankfilling.answer:
                score = blankfilling.weight
            else:
                score = 0
            bfanswer = BFAnswer(exam=exam, answer=answer, score=score, blankfilling=blankfilling)
            bfanswer.save()
    if 3 in answers:
        for subjective, value in zip(subjectives, answers[3]):
            answer = answers[3][value]
            subanswer = SubAnswer(exam=exam, answer=answer, subject=subjective)
            subanswer.save()
    return JsonResponse({"code": 200, "message": "接收成功"})


# 上传主观题
def get_subjective(request):
    params = json.loads(request.body)
    exam_id = params.get('exam_id')
    exam = Exam.objects.get(id=exam_id)
    # 获取与该考试相关的Subjective对象
    subjectives = Subjective.objects.filter(exam=exam)
    # 提取所有相关的SubAnswer的answer属性，并转化为列表
    subanswer_answers = [
        {'subjective_id': subjective.id, 'answer': subanswer.answer}
        for subjective in subjectives
        for subanswer in SubAnswer.objects.filter(subjective=subjective)
    ]
    return JsonResponse(subanswer_answers, safe=False)


# 存储主观题得分
@csrf_exempt  # 如果你不使用CSRF保护，或者确定你的请求不需要它
@require_http_methods(["POST"])  # 只允许POST请求
def update_subanswer_scores(request):
    if request.method == 'POST':
        # 假设你的POST请求的内容类型是application/json
        body = request.body
        try:
            # 解析JSON数据
            data = json.loads(body)
            exam_id = data.get('exam_id')
            scores_list = data.get('scores')

            if not exam_id or not isinstance(scores_list, list):
                # 验证失败，返回错误响应
                return JsonResponse({"error": "Invalid data format. 'exam_id' and 'scores' are required."}, status=400)

                # 查找Exam对象
            try:
                exam = Exam.objects.get(id=exam_id)
            except Exam.DoesNotExist:
                # Exam不存在，返回错误响应
                return JsonResponse({"error": "Exam not found."}, status=404)

                # 假设scores_list中的分数数量与exam对应的SubAnswer数量相同，并且顺序一致
            subanswers = SubAnswer.objects.filter(exam=exam)

            # 遍历分数列表和SubAnswer查询集，更新score
            for score, subanswer in zip(scores_list, subanswers):
                subanswer.score = score
                subanswer.save()

                # 返回成功响应
            return JsonResponse({"message": "Scores updated successfully."})
        except json.JSONDecodeError:
            # 解析JSON时出错，返回错误响应
            return JsonResponse({"error": "Failed to parse JSON data."}, status=400)

            # 如果不是POST请求，返回错误响应
    return JsonResponse({"error": "Method Not Allowed"}, status=405)


"""
# 判断选择题
def judge_choiceanswer(request, exam_id):
    # 假设前端传回的答案在POST请求中，键为'answer'
    if request.method == 'POST':
        # answer = request.POST.get('answer')      
        # 获取Choice对象和Exam对象
        exam = get_object_or_404(Exam, pk=exam_id)
        #choice_answers = list(ChoiceAnswer.objects.filter(exam=exam))
        choices = list(Choice.objects.filter(exam=exam))
        for choice in choices:
        # 假设Choice模型有一个字段correct_answer存储正确答案
            correct_answer = choice.answer
            choice_answer = ChoiceAnswer.objects.filter(choice=choice)
            answer = choice_answer.answer
        # 判断用户答案是否正确
            is_correct = (answer == correct_answer)

        # 创建一个新的ChoiceAnswer对象或更新现有的ChoiceAnswer对象（取决于你的业务逻辑）
        # 这里假设我们更新现有的ChoiceAnswer对象（假设已经存在一个与exam和choice关联的ChoiceAnswer对象）
        # 注意：这只是一个示例，你可能需要根据你的业务逻辑来处理多个ChoiceAnswer对象（比如为每个用户存储一个）
            choice_answer, created = ChoiceAnswer.objects.get_or_create(
                exam=exam,
                choice=choice,
                defaults={'answer': answer, 'score': 0}  # 如果创建新对象，使用默认值
            )
            # 更新得分
            if is_correct:
                choice_answer.score = choice.weight
            else:
                choice_answer.score = 0  # 答错得0分，或者根据需求设置其他值
            choice_answer.save()  # 保存更新后的ChoiceAnswer对象

            # 返回响应
            return JsonResponse({'message': 'Answer submitted', 'score': choice_answer.score})

        # 如果不是POST请求，返回错误响应
    return JsonResponse({'error': 'Invalid request method'}, status=405)


# 判断填空题
def judge_bfanswer(request, exam_id, blankfilling_id):
    if request.method == 'POST':
        answer = request.POST.get('answer')
        blankfilling = get_object_or_404(BlankFilling, pk=blankfilling_id)
        exam = get_object_or_404(Exam, pk=exam_id)
        correct_answer = BlankFilling.answer
        is_correct = (answer == correct_answer)
        blankfilling_answer, created = BFAnswer.objects.get_or_create(
            exam=exam,
            blankfilling=blankfilling,
            defaults={'answer': answer, 'score': 0}  # 如果创建新对象，使用默认值
        )
        if is_correct:
            blankfilling_answer.score = blankfilling.weight
        else:
            blankfilling_answer.score = 0  # 答错得0分，或者根据需求设置其他值
        blankfilling_answer.save()  # 保存更新后的ChoiceAnswer对象
        return JsonResponse({'message': 'Answer submitted', 'score': blankfilling_answer.score})
    return JsonResponse({'error': 'Invalid request method'}, status=405)
"""


# 计算总分
# @login_required
def calculate_exam_total_score(request):
    params = json.loads(request.body.decode())
    exam_id = params.get('exam_id')
    exam = Exam.objects.get(id=exam_id)
    # 计算选择题的总分
    choice_scores = ChoiceAnswer.objects.filter(exam=exam).aggregate(total=Sum('score'))['total'] or 0
    # 计算填空题的总分
    bf_scores = BFAnswer.objects.filter(exam=exam).aggregate(total=Sum('score'))['total'] or 0
    # 计算主观题的总分
    sub_scores = SubAnswer.objects.filter(exam=exam).aggregate(total=Sum('score'))['total'] or 0
    # 计算总分
    total_score = choice_scores + bf_scores + sub_scores
    examscore = ExamScore(exam=exam, score=total_score)
    examscore.save()
    return JsonResponse({'message': 'Total score calculated', 'total_score': total_score})


# # 上传作答记录
# def get_exam_answers(request):
#     # 获取考试对象
#     params = json.loads(request.body)
#     exam_id = params.get('exam_id')
#     exam = Exam.objects.get(id=exam_id)
#
#     # 提取ChoiceAnswer的answer属性
#     choice_answers = list(ChoiceAnswer.objects.filter(exam=exam).values_list('answer', flat=True))
#
#     # 提取BFAnswer的answer属性
#     bf_answers = list(BFAnswer.objects.filter(exam=exam).values_list('answer', flat=True))
#
#     # 假设Subjective也有一个answer字段（如果不是这样，请根据你的模型进行修改）
#     subjective_answers = list(SubAnswer.objects.filter(exam=exam).values_list('answer', flat=True))
#
#     # 将作答结果组合成一个字典
#     answers = {
#         'choice_answers': choice_answers,
#         'bf_answers': bf_answers,
#         'subjective_answers': subjective_answers,
#     }
#
#     return JsonResponse(answers)


"""
def exam_total_score(request, exam_id):
    # 获取指定的Exam对象
    exam = get_object_or_404(Exam, pk=exam_id)

    # 获取该Exam下所有ChoiceAnswer的总分
    # 我们假设ChoiceAnswer的score字段已经包含了每道题的得分
    total_score = ChoiceAnswer.objects.filter(choice__exam=exam).aggregate(total=Sum('score'))['total'] or 0
    total_score += BFAnswer.objects.filter(blankfilling__exam=exam).aggregate(total=Sum('score'))['total'] or 0
    total_score += SubAnswer.objects.filter(subjective__exam=exam).aggregate(total=Sum('score'))['total'] or 0
    # 将结果以JSON格式返回
    data = {
        'exam_name': exam.name,
        'total_score': total_score,
    }
    return JsonResponse(data)


def create_choice(request):
    content = "题干"
    weight = 3
    answer = "c"
    course = Course.objects.filter(name="高等数学").first()
    chapter = "第一章"
    choice = Choice(content=content, weight=weight, answer=answer,
                    course=course, chapter=chapter)
    choice.save()
    return HttpResponse("yes")


def create_blankfilling(request):
    content = "题干"
    weight = 3
    answer = "答案"
    course = Course.objects.filter(name="高等数学").first()
    chapter = "第一章"
    blankfilling = BlankFilling(content=content, weight=weight, answer=answer,
                                course=course, chapter=chapter)
    blankfilling.save()
    return HttpResponse("yes")


def create_subjective(request):
    content = "题干"
    weight = 3
    course = Course.objects.filter(name="高等数学").first()
    chapter = "第一章"
    subjective = Subjective(content=content, weight=weight,
                            course=course, chapter=chapter)
    subjective.save()
    return HttpResponse("yes")


def create_exam(request):
    name = "高数第一次测试"
    choice = Choice.objects.filter(course__name="高等数学").first()
    blankfilling = BlankFilling.objects.filter(course__name="高等数学").first()
    subjective = Subjective.objects.filter(course__name="高等数学").first()
    stu = Stu.objects.filter(name="韩雪").first()
    exam = Exam(name=name, choice=choice, blankfilling=blankfilling,
                subjective=subjective, stu=stu)
    exam.save()
    return HttpResponse("yes")
"""
