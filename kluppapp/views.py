from django.shortcuts import render, redirect, HttpResponse
from . import models
from django.contrib import messages
from django.utils.timezone import now
from datetime import date

current_user = ''
date_Choice = ''


def dashboard(request):
    return render(request, 'studentlist.html')

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
        global date_Choice
        date =  request.POST['date']
        academicyear = request.POST['Academicyear']
        semesterid = request.POST['Semesterid']
        date_Choice = request.POST['date']
        print("daeteeteeeeeeeeeeteteeeeee")
        print(date_Choice)
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
    return render(request, 'coursesChoice.html')




def attendancelist(request,c_id, s_id, hr_id):
    stu_list = models.StudentCourses.objects.filter(s_section=s_id,s_course_id=c_id).values()
    if request.method == "POST":
        present =  request.POST.getlist('checks[]')
        print(present)
        print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        if hr_id == '1-2':
            print(now)
            check = models.StudentAttendace.objects.filter(s_course_id=c_id,hrs_1_2=False, date=date_Choice).values()
            if check :
                i = 0
                for j in stu_list :
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    print(pora['student_username'] )
                    if pora['student_username'] in present:
                        print('yes')
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'])
                        update.hrs_1_2 = True
                        update.save()
                    else:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'])
                        update.hrs_1_2 = False 
                        update.save() 
                return HttpResponse('done1')  
            else:
                i = 0
                c_get = models.Courses.objects.get(course_id=c_id)
                for j in stu_list :
                    s_get = models.Student.objects.get(student_id =j['s_id_id'])
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_1_2=True)
                    else:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_1_2=False)
                    create.save()
                return HttpResponse('done2')
            
        elif hr_id == '3-4':
            check = models.StudentAttendace.objects.filter(s_course_id=c_id,date=date_Choice,hrs_3_4=False).values()
            if check :
                i = 0
                for j in stu_list :
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'])
                        update.hrs_3_4 = True
                        update.save()
                    else:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'])
                        update.hrs_3_4 = False 
                        update.save() 
                return HttpResponse('done1')  
            else:
                i = 0
                c_get = models.Courses.objects.get(course_id=c_id)
                for j in stu_list :
                    s_get = models.Student.objects.get(student_id =j['s_id_id'])
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_3_4=True)
                    else:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_3_4=False)
                    create.save()
                return HttpResponse('done2')
        elif hr_id == '5-6':
            check = models.StudentAttendace.objects.filter(s_course_id=c_id,date=date_Choice,hrs_5_6=False).values()
            if check :
                i = 0
                for j in stu_list :
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'])
                        update.hrs_5_6 = True
                        update.save()
                    else:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'])
                        update.hrs_5_6 = False
                        update.save()  
                return HttpResponse('done1')  
            else:
                i = 0
                c_get = models.Courses.objects.get(course_id=c_id)
                for j in stu_list :
                    s_get = models.Student.objects.get(student_id =j['s_id_id'])
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_5_6=True)
                    else:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_5_6=False)
                    create.save()
                return HttpResponse('done2')
        elif hr_id == '7-8':
            check = models.StudentAttendace.objects.filter(s_course_id=c_id,date=date_Choice,hrs_7_8=False).values()
            if check :
                i = 0
                for j in stu_list :
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'])
                        update.hrs_7_8 = True
                        update.save()
                    else:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'])
                        update.hrs_7_8 = False  
                        update.save()
                return HttpResponse('done1')  
            else:
                i = 0
                c_get = models.Courses.objects.get(course_id=c_id)
                for j in stu_list :
                    s_get = models.Student.objects.get(student_id =j['s_id_id'])
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_7_8=True)
                    else:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_7_8=False)
                    create.save()
                return HttpResponse('done2')
             
    else:
        data = []
        for ts in stu_list :
            stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
            data.append(stu)
        return render(request, 'attendancelist.html' , {'data':data})
    return render(request, 'attendancelist.html')

def courseslist(request):
    return render(request, 'courseslist.html')

def uploadmarks(request):
    return render(request, 'uploadmarks.html')

def studentlist(request, c_id, s_id):
    stu_list = models.StudentCourses.objects.filter(s_section=s_id,s_course_id=c_id).values()
    data = []
    for ts in stu_list :
        stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
        data.append(stu)
    return render(request, 'studentlist.html', {'data': data})
