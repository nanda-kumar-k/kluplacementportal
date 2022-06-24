from tkinter import N
from unicodedata import name
from . import views
from django.urls import path

app_name = 'kluppapp'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.login, name='login'),
    path('attendanceChoice/', views.attendanceChoice, name='attendanceChoice'),
    path('attendancelist/', views.attendancelist, name='attendancelist'),
    path('courseslist/', views.courseslist, name='courseslist'),
    path('uploadmarks/', views.uploadmarks, name='uploadmarks'),
    path('studentlist/', views.studentlist, name='studentlist')
]