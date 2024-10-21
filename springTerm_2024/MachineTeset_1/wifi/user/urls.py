from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # path('', views.user),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('adduser/', views.addUserView, name="adduser"),
    path('addstudent/', views.addStuView, name="addstudent"),
    path('addteacher/', views.addTeacherView, name="addteacher"),
    path('addadmin/', views.addAdminView, name="addadmin"),
    path('editstudent/', views.editStuView, name="editstu"),
    path('editteacher/', views.editTeacherView, name="editteacher"),
    path('editadmin/', views.editAdminView, name="editadmin"),
]
