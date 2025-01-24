from django.urls import path
from .views import random_poetry
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('random-poetry/', random_poetry, name='random-poetry'),
]

# 添加这行--- 允许所有的media文件被访问
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)