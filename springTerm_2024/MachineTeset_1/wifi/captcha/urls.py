from django.urls import path
from user import views

from . import views
app_name = 'captcha'

urlpatterns = [
    path('sendcaptcha/', views.send_captcha, name='captcha'),
    path('updatepassword1/', views.email_update_password, name='email_update_password'),
    path('updatepassword2/', views.password_update_password, name='password_update_password'),
    path('updateemail/', views.email_update_email, name='update_email'),
    path('updatephone/', views.phone_update, name='update_phone'),
]
