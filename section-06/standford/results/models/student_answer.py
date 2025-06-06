from django.db.models import *
from accounts.models.student import Student
from questions.models.exam_question import ExamQuestion
from questions.models.exam_choice import ExamChoice
from results.models.exam_attempt import ExamAttempt

class StudentAnswer(Model):
    student = ForeignKey(Student, on_delete=CASCADE, related_name='student_answers')
    question = ForeignKey(ExamQuestion, on_delete=CASCADE, related_name='student_answers')
    selected_choice = ForeignKey(ExamChoice, on_delete=CASCADE, related_name='student_answers')
    attempt = ForeignKey(ExamAttempt, on_delete=CASCADE, related_name='student_answers')

    def __str__(self):
        return "This is the answer %s  to the question %s attempted by %s" % \
            (self.selected_choice, self.question.question_text, self.student.user.username)