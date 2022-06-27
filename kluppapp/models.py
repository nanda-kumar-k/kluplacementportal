from django.db import models
import uuid
from django.utils.timezone import now

class Courses(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_code = models.CharField(max_length=50, default=None)
    course_name = models.TextField()
    
    def __str__(self):
        return self.course_name

class Faculty(models.Model):
    faculty_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    faculty_username = models.CharField(max_length=100, unique=True)
    faculty_password = models.CharField(max_length=50)
    faculty_email = models.EmailField()
    
    def __str__(self):
        return self.faculty_username

class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_name = models.CharField(max_length=200)
    student_username = models.CharField(max_length=200, unique=True)
    student_email = models.EmailField()
    degree = models.CharField(max_length=50)
    
    def __str__(self):
        return self.student_name

class FacultyCourses(models.Model):
    f_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    f_course_id= models.ForeignKey(Courses, on_delete=models.CASCADE)
    f_section = models.CharField(max_length=20, default=None)
    course_sem = models.CharField(max_length=20, default=None)
    course_year = models.CharField(max_length=20, default=None)
    f_degree = models.CharField(max_length=50, default=None)
    
    def __str__(self):
        return f'{self.f_id.faculty_username} Profile'


class StudentCourses(models.Model):
    s_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    s_course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    course_sem = models.CharField(max_length=20, default=None)
    course_year = models.CharField(max_length=20, default=None)
    course_teaching = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    s_section = models.CharField(max_length=20, default=None)
    PPE_in_1_marks = models.CharField(max_length=10,default=0)
    PPE_in_2_marks = models.CharField(max_length=10,default=0)
    PPE_in_3_marks = models.CharField(max_length=10,default=0)
    PPE_in_4_marks = models.CharField(max_length=10,default=0)
    PPE_in_5_marks = models.CharField(max_length=10,default=0)
    End_exam_marks = models.CharField(max_length=10,default=0)
    
    
    def __str__(self):
        return self.s_id.student_name
    
class StudentAttendace(models.Model):
    s_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    s_course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    hrs_1_2 = models.BooleanField(default=False)
    hrs_3_4 = models.BooleanField(default=False)
    hrs_5_6 = models.BooleanField(default=False)
    hrs_7_8 = models.BooleanField(default=False)
    
    def __str__(self):
        return self.s_id.student_name
    
    

    
    
    
    
    
