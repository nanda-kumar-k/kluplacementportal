from tkinter import N
from unicodedata import name
from . import views
from django.urls import path

app_name = 'kluppapp'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.login, name='login'),
    path('coursesChoice/', views.coursesChoice, name='coursesChoice'),
    path('attendancelist/<uuid:c_id>/<slug:s_id>/<str:hr_id>', views.attendancelist, name='attendancelist'),
    path('courseslist/', views.courseslist, name='courseslist'),
    path('uploadmarks/', views.uploadmarks, name='uploadmarks'),
    path('studentlist/<uuid:c_id>/<slug:s_id>/', views.studentlist, name='studentlist')
]