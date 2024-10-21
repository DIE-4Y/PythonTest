from django.db import models


# Create your models here.
# 验证码
class CaptchaModel(models.Model):
    email = models.EmailField(unique=True, verbose_name='邮箱')
    captcha = models.TextField(max_length=5, verbose_name='验证码')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
