from django.shortcuts import render, redirect, HttpResponse
from . import models
from django.contrib import messages

current_user = ''

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    if request.method == "POST":
        user = request.POST['username']
        pwd = request.POST['password']
        check = models.Faculty.objects.filter(faculty_username=user, faculty_password=pwd).values()
        if check:
            global current_user
            current_user = check[0]['faculty_id']
            return redirect('kluppapp:dashboard')
        else:
            messages.error(request, f"Invalid UserName and Password...! Try Again ")
            return render(request, "login.html")
        
    return render(request, 'login.html')

def coursesChoice(request):
    if request.method == "POST":
        date =  request.POST['date']
        academicyear = request.POST['Academicyear']
        semesterid = request.POST['Semesterid']
        if date and academicyear and semesterid :
            f_all_courses= models.FacultyCourses.objects.filter(
                f_id=current_user,course_sem=semesterid,course_year=academicyear).values()
            data = []
            for tc in f_all_courses:
                temp = tc
                course = models.Courses.objects.filter(course_id=tc['f_course_id_id']).values()[0]
                temp['course_name'] = course['course_name']
                temp['course_code'] = course['course_code']
                data.append(temp)
            return render(request, 'courseslist.html', {'data':data})
        else:
            messages.info(request, f"All fileds are required...!")
            return render(request, 'coursesChoice.html')
        print(date)
        print(academicyear)
        print(semesterid)
        return HttpResponse("jjjj")
        
    return render(request, 'coursesChoice.html')

def attendancelist(request):
    return render(request, 'attendancelist.html')

def courseslist(request):
    return render(request, 'courseslist.html')

def uploadmarks(request):
    return render(request, 'uploadmarks.html')

def studentlist(request):
    return render(request, 'studentlist.html')
