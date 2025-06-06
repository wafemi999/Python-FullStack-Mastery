from django.contrib import admin
from results.models.student_answer import StudentAnswer
from results.models.exam_attempt import ExamAttempt
from results.models.result import Result

# Register your models here.
admin.site.register(StudentAnswer)
admin.site.register(ExamAttempt)
admin.site.register(Result)