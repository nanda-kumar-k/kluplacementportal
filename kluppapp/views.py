import re
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')

def attendanceChoice(request):
    return render(request, 'attendanceChoice.html')

def attendancelist(request):
    return render(request, 'attendancelist.html')

def courseslist(request):
    return render(request, 'courseslist.html')

def uploadmarks(request):
    return render(request, 'uploadmarks.html')

def studentlist(request):
    return render(request, 'studentlist.html')
