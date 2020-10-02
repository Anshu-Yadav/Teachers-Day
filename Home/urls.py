from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('quotes', views.quotes, name="quotes"),
    path('teacherlogin', views.TeacherLogin, name="TeacherLogin"),
    path('teacherlogout', views.TeacherLogout, name="TeacherLogout"),
]