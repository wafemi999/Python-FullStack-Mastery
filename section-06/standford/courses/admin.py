from django.contrib import admin
from courses.models.course import Course
from courses.models.exam import Exam

# Register your models here.
admin.site.register(Course)
admin.site.register(Exam)