from django import forms
from django.core import validators
from .models import Article

class MessageBoardForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=50, label="标题",
                            error_messages = {"min_length":"标题至少3个字","max_length":"标题最大50个字"})
    content = forms.CharField(widget=forms.Textarea, label="内容")
    email= forms.EmailField(label="邮箱")


# validator进行表单验证
class RegisterForm(forms.Form):
    telephone = forms.CharField(validators=[validators.RegexValidator(r"1[3456789]\d{9}", message="手机号码格式错误")])
    pwd1 = forms.CharField(max_length=50)
    pwd2 = forms.CharField(max_length=50)
    # 针对某个字段进行验证
    def clean_telephone(self):
        telephone = self.cleaned_data.get("telephone")
        if telephone == "18888888888":
            raise forms.ValidationError("号码已存在！")
    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get("pwd1")
        pwd2 = cleaned_data.get("pwd2")
        if pwd1 != pwd2:
            raise forms.ValidationError("两次密码不一致！")
        else:
            return cleaned_data

# 从model继承Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        # 只继承一部分
        #fields = ['title', 'content']
        # 指定自己的错误信息
        error_messages={
            "title": {"required": "不能为空"},
            "category": {"required": "不能为空"}
        }