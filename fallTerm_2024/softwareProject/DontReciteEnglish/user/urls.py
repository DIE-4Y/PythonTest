from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('sendcaptcha/', views.sendCaptcha, name='sendCaptcha'),
    path('login/', views.userLogin, name='userLogin'),
    path('emaillogin/', views.emailLogin, name='emailLogin'),
    path('cpatchalogin/', views.captchaLogin, name='captchaLogin'),
    path('logout/', views.userLogout, name='userLogout'),
    path('getnifor/', views.getInfor, name='getInfor'),
    path('uploadphoto/', views.uploadPhoto, name='uploadPhoto'),
    path('emailupdatepassword/', views.emailUpdatePassword, name='emailUpdatePassword'),
    path('passwordupdatepassword/', views.passwordUpdatePassword, name='passwordUpdatePassword'),
    path('emailupdateemail/', views.emailUpdateEmail, name='emailUpdateEmail'),
    path('updatename/', views.updateName, name='updateName'),
    path('nainongswitch/', views.updateNainong, name='nainongswitch'),
    path('userSignIn/', views.userSignIn, name='userSignIn'),
    path('setGaol/', views.setGaol, name='setGaol'),
]

# 添加这行--- 允许所有的media文件被访问
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
