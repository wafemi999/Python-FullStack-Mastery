from django.db.models import *
from accounts.models.student import Student
from courses.models.exam import Exam

class Result(Model):
    student = ForeignKey(Student, on_delete=CASCADE, related_name='results')
    exam = ForeignKey(Exam, on_delete=CASCADE, related_name='results')
    score = IntegerField(default=0)