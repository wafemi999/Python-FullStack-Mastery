from rest_framework.serializers import *
from accounts.models.student import Student

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['user', 'student_id']