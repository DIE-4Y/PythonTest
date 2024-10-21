from django.contrib import admin
from .models import BlogCategory, Blog


# Register your models here.
# 配置被管理类
class BlogCategoryAdmin(admin.ModelAdmin):
    # list_display是展示出来能被编辑的字段
    # list_display里边的必须是类的属性
    list_display = ["name"]

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "pub_date", "category", "author"]

# 注册能被管理的类
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)