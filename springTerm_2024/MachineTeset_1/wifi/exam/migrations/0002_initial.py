# Generated by Django 5.0.3 on 2024-06-15 13:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exam', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to=settings.AUTH_USER_MODEL, verbose_name='考试学生'),
        ),
        migrations.AddField(
            model_name='choiceanswer',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ChoiceAnswers', to='exam.exam', verbose_name='选择题作答'),
        ),
        migrations.AddField(
            model_name='choice',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='exam.exam', verbose_name='考试'),
        ),
        migrations.AddField(
            model_name='blankfilling',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blankFillings', to='exam.exam', verbose_name='考试'),
        ),
        migrations.AddField(
            model_name='bfanswer',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BFAnswers', to='exam.exam', verbose_name='填空题作答'),
        ),
        migrations.AddField(
            model_name='examscore',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam'),
        ),
        migrations.AddField(
            model_name='subanswer',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam'),
        ),
        migrations.AddField(
            model_name='subjective',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjectives', to='exam.exam', verbose_name='考试'),
        ),
        migrations.AddField(
            model_name='subanswer',
            name='subjective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.subjective'),
        ),
    ]
