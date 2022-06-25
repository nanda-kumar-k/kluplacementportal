from django.db import models
import uuid


class Courses(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    
    def __str__(self):
        return f'{self.f_id.faculty_username} Profile'


class StudentCourses(models.Model):
    s_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    s_course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    course_taken = models.IntegerField()
    course_teaching = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    PPE_in_1_marks = models.IntegerField()
    PPE_in_2_marks = models.IntegerField()
    PPE_in_3_marks = models.IntegerField()
    PPE_in_4_marks = models.IntegerField()
    PPE_in_5_marks = models.IntegerField()
    End_exam_marks = models.IntegerField()
    
    
    def __str__(self):
        return self.s_id.student_name
    
class StudentAttendace(models.Model):
    s_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    s_course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    date = models.DateTimeField()
    hrs_1_2 = models.BooleanField(default=False)
    hrs_3_4 = models.BooleanField(default=False)
    hrs_5_6 = models.BooleanField(default=False)
    hrs_7_8 = models.BooleanField(default=False)
    
    def __str__(self):
        return self.s_id.student_name
    
    

    
    
    
    
    

