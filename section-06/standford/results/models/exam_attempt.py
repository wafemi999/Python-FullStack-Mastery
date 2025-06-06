from django.db.models import *
from accounts.models.student import Student
from courses.models.exam import Exam

class ExamAttempt(Model):
    student = ForeignKey(Student, on_delete=CASCADE, related_name='exam_attempts')
    exam = ForeignKey(Exam, on_delete=CASCADE, related_name='exam_attempts')
    score = IntegerField(default=0)
    attempt_at = DateTimeField(auto_created=True)

    def __str__(self):
        return "This is exam %s was attempted by %s at %s" % \
            (self.exam.title, self.student.user.username, self.attempt_at)