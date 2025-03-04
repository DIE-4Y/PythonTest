# Generated by Django 5.0.3 on 2024-05-21 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('study', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.course')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('answer', models.TextField()),
                ('tag', models.CharField(choices=[('SingleChoice', '单选题'), ('MultipleChoice', '多选题'), ('Judge', '判断题'), ('ShortAnswer', '简答题'), ('Vocabulary', '应用题')], max_length=14)),
                ('weight', models.SmallIntegerField(default=0)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.chapter')),
                ('examination', models.ManyToManyField(related_name='questions', to='studyTest.examination')),
            ],
        ),
        migrations.AddField(
            model_name='examination',
            name='question',
            field=models.ManyToManyField(related_name='examinations', to='studyTest.question'),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.SmallIntegerField(default=0)),
                ('examination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyTest.examination')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
            ],
        ),
    ]
