from accounts.models.user import StandfordUser
from django.db.models import CharField, OneToOneField, Model, CASCADE

class Admin(Model):
    user = OneToOneField(StandfordUser, on_delete=CASCADE)
    department = CharField(max_length=255)

    def __str__(self) -> str:
        return self.user.username
