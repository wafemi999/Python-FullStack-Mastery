from django.contrib import admin
from accounts.models.user import StandfordUser
from accounts.models.admin import Admin
from accounts.models.student import Student

# Register your models here.
admin.site.register(StandfordUser)
admin.site.register(Student)
admin.site.register(Admin)
