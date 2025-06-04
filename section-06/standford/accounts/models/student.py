from accounts.models.user import StandfordUser
from django.db.models import CharField, OneToOneField, Model, CASCADE

class Student(Model):
    user = OneToOneField(StandfordUser, on_delete=CASCADE)
    student_id = CharField(max_length=6)

    def __str__(self) -> str:
        return self.user.username
