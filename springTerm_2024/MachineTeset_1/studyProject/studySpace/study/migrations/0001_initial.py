# Generated by Django 5.0.3 on 2024-05-21 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('origin_url', models.URLField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=20, unique=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.chapter')),
                ('videos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.video')),
            ],
        ),
    ]