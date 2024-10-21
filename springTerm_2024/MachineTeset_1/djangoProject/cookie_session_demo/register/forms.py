from django import forms
from .models import CaptchaModel
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2, error_messages={"required": "请传入用户名",
                                                                            "max_length": "用户名长度应在2~20之间",
                                                                            "min_length": "用户名长度应在2~20之间"})
    email = forms.EmailField(error_messages={"required": "请传入邮箱", "invalid": "邮箱格式不正确"})
    captcha = forms.CharField(max_length=4, min_length=4, error_messages={"required": "请输入验证码",
                                                                          "max_length": "验证码只有四位",
                                                                          "min_length": "验证码需要四位"})
    password = forms.CharField(max_length=20, min_length=6, error_messages={"required": "请输入密码"})
    # 验证字段
    def clean_email(self):
        email = self.cleaned_data.get('email')
        exits = User.objects.filter(email=email).exists()
        if exits:
            raise forms.ValidationError("邮箱已经存在")
        return email

    def clean_captcha(self):
        email = self.cleaned_data.get('email')
        captcha = self.cleaned_data.get('captcha')

        captcha_model = CaptchaModel.objects.filter(email=email, captcha=captcha).first()
        if not captcha_model:
            raise forms.ValidationError("验证码和邮箱不匹配！")
        captcha_model.delete()
        return captcha


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={"required": "请传入邮箱", "invalid": "邮箱格式不正确"})
    password = forms.CharField(max_length=20, min_length=6, error_messages={"required": "请输入密码"})
    remember = forms.IntegerField(required=False)