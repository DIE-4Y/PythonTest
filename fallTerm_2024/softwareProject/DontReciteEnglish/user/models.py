from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户模型
class User(AbstractUser):
    username = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField(unique=True)
    # photo = models.ImageField(upload_to='media', null=True)
    photo = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=40, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return (self.username, self.email)


# 验证码模型
class Captcha(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=4)

    class Meta:
        db_table = 'captcha'

    def __str__(self):
        return self.email
