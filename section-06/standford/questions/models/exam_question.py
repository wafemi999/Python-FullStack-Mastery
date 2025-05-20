from django.db.models import *
from courses.models.exam import Exam

class ExamQuestion(Model):
    exam = OneToOneField(Exam, on_delete=CASCADE)
    question_text = CharField(max_length=500, default="free question")
    mark = IntegerField()