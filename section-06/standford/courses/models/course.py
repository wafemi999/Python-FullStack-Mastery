from django.db.models import *

class Course(Model):
    name = CharField(max_length=100)
    code = CharField(unique=True)
    description = CharField(max_length=600)

