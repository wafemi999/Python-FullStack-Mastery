from django.db.models import *
from courses.models.course import Course
from accounts.models.admin import Admin

class Exam(Model):
    course = ForeignKey(Course, related_name='exams', on_delete=CASCADE)
    admin = ForeignKey(Admin, related_name='exams', on_delete=CASCADE)
    title = SlugField(primary_key=True)
    total_marks = IntegerField()
    date = DateTimeField()
    duration_minutes = IntegerField()

    def __str__(self) -> str:
        return self.title