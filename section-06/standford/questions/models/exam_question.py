from django.db.models import *
from courses.models.exam import Exam

class ExamQuestion(Model):
    exam = ForeignKey(Exam, related_name='exam_questions', on_delete=CASCADE)
    question_text = CharField(max_length=500, default="free question")
    mark = IntegerField()

    def __str__(self) -> str:
        return self.question_text