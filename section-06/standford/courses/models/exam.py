from django.db.models import *
from courses.models.course import Course

class Exam(Model):
    course = ForeignKey(Course, on_delete=CASCADE)
    title = SlugField(primary_key=True)
    total_marks = IntegerField()
    date = DateTimeField()
    duration_minutes = IntegerField()

    def __str__(self) -> str:
        return self.title