from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.


class CaptchaModel(models.Model):
    email = models.EmailField(unique=True)
    captcha = models.TextField(max_length=5)
    create_time = models.DateTimeField(auto_now_add=True)

class BlogCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name="博客种类")

    # 管理系统展示模型的字段
    def __str__(self):
        return self.name

    class Meta:
        # verbose_name设置名称,在管理界面可以看见,Meta下的是设置类的名称,
        # 单数时的名称
        verbose_name = "博客种类"
        # 复数时的名称
        verbose_name_plural = verbose_name

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name="种类")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name

class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
