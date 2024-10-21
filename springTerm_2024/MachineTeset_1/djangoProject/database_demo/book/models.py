from django.db import models

# Create your models here.


# 不能再结尾加上','不然会认为模块结束
# 未定义主键,会自动添加一个automfield的主键
class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.FloatField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

# Meta,可对一个模式进行内部修改,包括但不限于排序,表重命名
    class Meta:
        ordering = ("-pub_date", "price")