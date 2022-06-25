from django.contrib import admin
from . import models


admin.site.register(models.Courses)
admin.site.register(models.Faculty)
admin.site.register(models.FacultyCourses)
admin.site.register(models.Student)
admin.site.register(models.StudentCourses)
admin.site.register(models.StudentAttendace)
