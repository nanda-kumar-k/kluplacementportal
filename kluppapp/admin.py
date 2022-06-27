from django.contrib import admin
from . import models
from import_export.admin import ImportExportMixin

class CoursesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['course_id', 'course_code', 'course_name']

class FacultyAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['faculty_id', 'faculty_username', 'faculty_password','faculty_email']

class StudentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['student_id', 'student_name', 'student_username','student_email','degree']

class FacultyCoursesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['f_id', 'f_course_id', 'f_section','course_sem','course_year','f_degree']
    
class StudentCoursesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['s_id', 's_course_id', 'course_sem','course_year','course_teaching','s_section',
                    'PPE_in_1_marks','PPE_in_2_marks','PPE_in_3_marks','PPE_in_4_marks','PPE_in_5_marks','End_exam_marks',]

class StudentAttendaceAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['s_id', 's_course_id', 'date','hrs_1_2','hrs_3_4','hrs_5_6', 'hrs_7_8']

admin.site.register(models.Courses, CoursesAdmin)
admin.site.register(models.Faculty, FacultyAdmin)
admin.site.register(models.FacultyCourses, FacultyCoursesAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.StudentCourses, StudentCoursesAdmin)
admin.site.register(models.StudentAttendace, StudentAttendaceAdmin)


