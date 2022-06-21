from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')
