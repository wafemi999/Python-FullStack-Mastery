from django.db.models import *

class Course(Model):
    name = CharField(max_length=100)
    code = CharField(max_length=7, unique=True)
    description = CharField(max_length=600)

    def __str__(self):
        return "%s - %s" % (self.name, self.code)