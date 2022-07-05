from unicodedata import numeric
from django.shortcuts import render, redirect, HttpResponse
from . import models
from django.contrib import messages
from django.utils.timezone import now
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import metrics
from django.templatetags.static import static

current_user = ''
date_Choice = ''
current_user_id = ''

def dashboard(request):
    if not current_user or not current_user_id :
        return redirect('kluppapp:login')
    data = []
    data.append("temp")
    data.append(current_user_id)
    return render(request, 'dashboard.html', {'data': data})

def login(request):
    if request.method == "POST":
        user = request.POST['username']
        pwd = request.POST['password']
        check = models.Faculty.objects.filter(faculty_username=user, faculty_password=pwd).values()
        if check:
            global current_user, current_user_id
            current_user = check[0]['faculty_id']
            current_user_id = user
            return redirect('kluppapp:dashboard')
        else:
            messages.error(request, f"Invalid UserName and Password...! Try Again ")
            return render(request, "login.html")
        
    return render(request, 'login.html')

def coursesChoice(request):
    if not current_user or not current_user_id :
        return redirect('kluppapp:login')
    data = []
    data.append("temp")
    data.append(current_user_id)
    if request.method == "POST":
        global date_Choice
        date =  request.POST['date']
        academicyear = request.POST['Academicyear']
        semesterid = request.POST['Semesterid']
        date_Choice = request.POST['date']
        if date and academicyear and semesterid :
            f_all_courses= models.FacultyCourses.objects.filter(
                f_id=current_user,course_sem=semesterid,course_year=academicyear).values()
            data = []
            temp_data = []
            for tc in f_all_courses:
                temp = tc
                course = models.Courses.objects.filter(course_id=tc['f_course_id_id']).values()[0]
                temp['course_name'] = course['course_name']
                temp['course_code'] = course['course_code']
                temp_data.append(temp)
            data.append(temp_data)
            data.append(current_user_id)
            return render(request, 'courseslist.html', {'data':data})
        else:
            messages.info(request, f"All fileds are required...!")
            return render(request, 'coursesChoice.html', {'data':data})
    
    return render(request, 'coursesChoice.html', {'data':data})




def attendancelist(request,c_id, s_id, hr_id):
    if not current_user or not current_user_id :
        return redirect('kluppapp:login')
    stu_list = models.StudentCourses.objects.filter(s_section=s_id,s_course_id=c_id).values()
    if request.method == "POST":
        present =  request.POST.getlist('checks[]')
        if hr_id == '1-2':
            check = models.StudentAttendace.objects.filter(s_course_id=c_id, date=date_Choice).values()
            if check :
                i = 0
                for j in stu_list :
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    print(pora['student_username'] )
                    if pora['student_username'] in present:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'],date=date_Choice,s_course_id=c_id)
                        update.hrs_1_2 = True
                        update.save()
                    else:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'],date=date_Choice,s_course_id=c_id)
                        update.hrs_1_2 = False 
                        update.save()
                messages.success(request, f"Attendance updated successfully...!") 
                return redirect('kluppapp:coursesChoice')  
            else:
                i = 0
                c_get = models.Courses.objects.get(course_id=c_id)
                for j in stu_list :
                    s_get = models.Student.objects.get(student_id =j['s_id_id'])
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_1_2=True,date=date_Choice)
                    else:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_1_2=False,date=date_Choice)
                    create.save()
                messages.success(request, f"Attendance updated successfully...!")
                return redirect('kluppapp:coursesChoice')
            
        elif hr_id == '3-4':
            check = models.StudentAttendace.objects.filter(s_course_id=c_id,date=date_Choice).values()
            if check :
                i = 0
                for j in stu_list :
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'],date=date_Choice,s_course_id=c_id)
                        update.hrs_3_4 = True
                        update.save()
                    else:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'],date=date_Choice,s_course_id=c_id)
                        update.hrs_3_4 = False 
                        update.save()
                messages.success(request, f"Attendance updated successfully...!") 
                return redirect('kluppapp:coursesChoice')  
            else:
                i = 0
                c_get = models.Courses.objects.get(course_id=c_id)
                for j in stu_list :
                    s_get = models.Student.objects.get(student_id =j['s_id_id'])
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_3_4=True,date=date_Choice)
                    else:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_3_4=False,date=date_Choice)
                    create.save()
                messages.success(request, f"Attendance updated successfully...!")
                return redirect('kluppapp:coursesChoice')
        elif hr_id == '5-6':
            check = models.StudentAttendace.objects.filter(s_course_id=c_id,date=date_Choice).values()
            if check :
                i = 0
                for j in stu_list :
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'],date=date_Choice,s_course_id=c_id)
                        update.hrs_5_6 = True
                        update.save()
                    else:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'],date=date_Choice,s_course_id=c_id)
                        update.hrs_5_6 = False
                        update.save() 
                messages.success(request, f"Attendance updated successfully...!") 
                return redirect('kluppapp:coursesChoice')  
            else:
                i = 0
                c_get = models.Courses.objects.get(course_id=c_id)
                for j in stu_list :
                    s_get = models.Student.objects.get(student_id =j['s_id_id'])
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_5_6=True,date=date_Choice)
                    else:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_5_6=False,date=date_Choice)
                    create.save()
                messages.success(request, f"Attendance updated successfully...!")
                return redirect('kluppapp:coursesChoice')
        elif hr_id == '7-8':
            check = models.StudentAttendace.objects.filter(s_course_id=c_id,date=date_Choice).values()
            if check :
                i = 0
                for j in stu_list :
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'],date=date_Choice,s_course_id=c_id)
                        update.hrs_7_8 = True
                        update.save()
                    else:
                        update = models.StudentAttendace.objects.get(s_id=j['s_id_id'],date=date_Choice,s_course_id=c_id)
                        update.hrs_7_8 = False  
                        update.save()
                messages.success(request, f"Attendance updated successfully...!")
                return redirect('kluppapp:coursesChoice') 
            else:
                i = 0
                c_get = models.Courses.objects.get(course_id=c_id)
                for j in stu_list :
                    s_get = models.Student.objects.get(student_id =j['s_id_id'])
                    pora = models.Student.objects.filter(student_id=j['s_id_id']).values()[0]
                    if pora['student_username'] in present:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_7_8=True,date=date_Choice)
                    else:
                        create = models.StudentAttendace(s_id=s_get,s_course_id=c_get,hrs_7_8=False,date=date_Choice)
                    create.save()
                messages.success(request, f"Attendance updated successfully...!")
                return redirect('kluppapp:coursesChoice')
             
    else:
        data = []
        temp_data = []
        if hr_id == '1-2':
            check = models.StudentAttendace.objects.filter(s_course_id=c_id,hrs_1_2=False, date=date_Choice).values()
            for ts in stu_list :
                if check :
                    find = models.StudentAttendace.objects.filter(s_id_id=ts['s_id_id'],s_course_id=c_id,date=date_Choice).values()[0]
                    stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                    stu['pora'] = find['hrs_1_2']
                    temp_data.append(stu)
                else:
                    stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                    temp_data.append(stu)
        elif hr_id == '3-4':
            check = models.StudentAttendace.objects.filter(s_course_id=c_id,hrs_1_2=False, date=date_Choice).values()
            for ts in stu_list :
                if check :
                    find = models.StudentAttendace.objects.filter(s_id_id=ts['s_id_id'],s_course_id=c_id,date=date_Choice).values()[0]
                    stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                    stu['pora'] = find['hrs_3_4']
                    temp_data.append(stu)
                else:
                    stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                    temp_data.append(stu)
        elif hr_id == '5-6':
            check = models.StudentAttendace.objects.filter(s_course_id=c_id,hrs_1_2=False, date=date_Choice).values()
            for ts in stu_list :
                if check :
                    find = models.StudentAttendace.objects.filter(s_id_id=ts['s_id_id'],s_course_id=c_id,date=date_Choice).values()[0]
                    stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                    stu['pora'] = find['hrs_5_6']
                    temp_data.append(stu)
                else:
                    stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                    temp_data.append(stu)
        elif hr_id == '7-8':
            check = models.StudentAttendace.objects.filter(s_course_id=c_id,hrs_1_2=False, date=date_Choice).values()
            for ts in stu_list :
                if check :
                    find = models.StudentAttendace.objects.filter(s_id_id=ts['s_id_id'],s_course_id=c_id,date=date_Choice).values()[0]
                    stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                    stu['pora'] = find['hrs_7_8']
                    temp_data.append(stu)
                else:
                    stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                    temp_data.append(stu)
        
        data.append(temp_data)
        data.append(current_user_id)
        return render(request, 'attendancelist.html' , {'data':data})
    return render(request, 'attendancelist.html')

def courseslist(request):
    return render(request, 'courseslist.html')



def uploadmarks(request,c_id, s_id, ex_id):
    if not current_user or not current_user_id :
        return redirect('kluppapp:login')
    stu_list = models.StudentCourses.objects.filter(s_section=s_id,s_course_id=c_id).values()
    if request.method == "POST":
        if ex_id == 'ppe-1':
            i = 0
            for ts in stu_list:
                update = models.StudentCourses.objects.get(s_id=ts['s_id_id'],s_section=s_id,s_course_id=c_id)
                d = request.POST.getlist('checks[]')
                update.PPE_in_1_marks= d[i]
                update.save()
                i = i+1
            messages.success(request, f"PPE in 1 marks updated successfully...!")
            return redirect('kluppapp:coursesChoice')
        elif ex_id == 'ppe-2':
            i = 0
            for ts in stu_list:
                update = models.StudentCourses.objects.get(s_id=ts['s_id_id'],s_section=s_id,s_course_id=c_id)
                d = request.POST.getlist('checks[]')
                update.PPE_in_2_marks= d[i]
                update.save()
                i = i+1
            messages.success(request, f"PPE in 2 marks updated successfully...!")
            return redirect('kluppapp:coursesChoice')
        elif ex_id == 'ppe-3':
            i = 0
            for ts in stu_list:
                update = models.StudentCourses.objects.get(s_id=ts['s_id_id'],s_section=s_id,s_course_id=c_id)
                d = request.POST.getlist('checks[]')
                update.PPE_in_3_marks= d[i]
                update.save()
                i = i+1
            messages.success(request, f"PPE in 3 marks updated successfully...!")
            return redirect('kluppapp:coursesChoice')
        if ex_id == 'ppe-4':
            i = 0
            for ts in stu_list:
                update = models.StudentCourses.objects.get(s_id=ts['s_id_id'],s_section=s_id,s_course_id=c_id)
                d = request.POST.getlist('checks[]')
                update.PPE_in_4_marks= d[i]
                update.save()
                i = i+1
            messages.success(request, f"PPE in 4 marks updated successfully...!")
            return redirect('kluppapp:coursesChoice')
        if ex_id == 'ppe-5':
            i = 0
            for ts in stu_list:
                update = models.StudentCourses.objects.get(s_id=ts['s_id_id'],s_section=s_id,s_course_id=c_id)
                d = request.POST.getlist('checks[]')
                update.PPE_in_5_marks= d[i]
                update.save()
                i = i+1
            messages.success(request, f"PPE in 5 marks updated successfully...!")
            return redirect('kluppapp:coursesChoice')
        if ex_id == 'end-exam':
            i = 0
            for ts in stu_list:
                update = models.StudentCourses.objects.get(s_id=ts['s_id_id'],s_section=s_id,s_course_id=c_id)
                d = request.POST.getlist('checks[]')
                update.End_exam_marks= d[i]
                update.save()
                i = i+1
            messages.success(request, f"End Exam marks updated successfully...!")
            return redirect('kluppapp:coursesChoice')
    else:
        data = []
        temp_data = []
        if ex_id == 'ppe-1':
            for ts in stu_list :
                stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                stu['marks'] = ts['PPE_in_1_marks']
                temp_data.append(stu)
        elif ex_id == 'ppe-2':
            for ts in stu_list :
                stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                stu['marks'] = ts['PPE_in_2_marks']
                temp_data.append(stu)
        elif ex_id == 'ppe-3':
            for ts in stu_list :
                stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                stu['marks'] = ts['PPE_in_3_marks']
                temp_data.append(stu)
        elif ex_id == 'ppe-4':
            for ts in stu_list :
                stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                stu['marks'] = ts['PPE_in_4_marks']
                temp_data.append(stu)
        elif ex_id == 'ppe-5':
            for ts in stu_list :
                stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                stu['marks'] = ts['PPE_in_5_marks']
                temp_data.append(stu)
        if ex_id == 'end-exam':
            for ts in stu_list :
                stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
                stu['marks'] = ts['End_exam_marks']
                temp_data.append(stu)
    
        data.append(temp_data)
        data.append(current_user_id)
        return render(request, 'uploadmarks.html' , {'data':data})
    return render(request, 'uploadmarks.html')

def studentlist(request, c_id, s_id):
    if not current_user or not current_user_id :
        return redirect('kluppapp:login')
    stu_list = models.StudentCourses.objects.filter(s_section=s_id,s_course_id=c_id).values()
    data = []
    temp_data = []
    for ts in stu_list :
        stu = models.Student.objects.filter(student_id=ts['s_id_id']).values()[0]
        temp_data.append(stu)
    data.append(temp_data)
    data.append(current_user_id)
    return render(request, 'studentlist.html', {'data': data})

def logout(request):
    global current_user, current_user_id, date_Choice
    current_user = ''
    current_user_id = ''
    date_Choice = ''
    return redirect('kluppapp:login')

from sklearn.utils.validation import check_array

def Prediction(request):
    if not current_user or not current_user_id :
        return redirect('kluppapp:login')
    if request.method == "POST":
        ssc =  float(request.POST['ssc'])
        inter_marks = float(request.POST['inter_marks'])
        bteach_marks = float(request.POST['bteach_marks'])
        etest = float(request.POST['etest'])
        
        url = static("placement_data.csv") 
        data = pd.read_csv("http://127.0.0.1:8000/media/placement_data.csv")
        # data=pd.read_csv(r"C:\Users\mvr_n\Downloads\placement_data.csv")
        # data=pd.read_csv(url)
        print(data.dtypes)
        data.dropna(inplace=True)
        data=data.drop(['sl_no','gender','spcial_t','status'],axis=1)
        #print(data.head())
        '''sns.heatmap(data.isnull())
        x=data.drop('salry',axis=1)
        y=data["salary"]
        x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.30)'''
        x=data.drop('salary',axis=1)
        #print(x.head())
        y=data['salary']
        #print(y.head())
        x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.30)
        model=LinearRegression()
        model.fit(x_train,y_train)
        # X = np.array([s_no]).reshape(-1, 1)
        # array = check_array(X)
        # d = check_array(s_no, dtype='numeric').reshape(-1, 1)
        predictions=model.predict(np.array([ssc,inter_marks,bteach_marks,etest]).reshape(1, -1))
        #print(predictions)
        #error=np.sqrt(metrics.mean_absolute_error(y_test,predictions))
        #print(error)
        messages.success(request, f"Prediction of the salary is {predictions}") 
        return render(request, "prediction.html")
    
    return render(request, "prediction.html")