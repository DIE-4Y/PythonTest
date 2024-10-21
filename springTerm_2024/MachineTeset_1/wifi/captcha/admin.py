from django.contrib import admin
from .models import CaptchaModel
# Register your models here.



class CaptchaModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'captcha']
    search_fields = ['email', 'captcha']

admin.site.register(CaptchaModel, CaptchaModelAdmin)