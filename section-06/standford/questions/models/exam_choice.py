from django.db.models import *
from questions.models.exam_question import ExamQuestion

class ExamChoice(Model):
    question = ForeignKey(ExamQuestion, related_name='exam_choices', on_delete=CASCADE)
    choice_text = CharField(max_length=200)
    is_correct = BooleanField(default=False)

    def __str__(self):
        return self.choice_text