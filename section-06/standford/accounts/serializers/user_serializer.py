from accounts.models.admin import Admin
from accounts.models.student import Student
from rest_framework.serializers import *
from accounts.models.user import StandfordUser

class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)
    role = ChoiceField(choices=['student', 'admin'], write_only=True)
    student_id = CharField(required=False, allow_blank=True)
    department = CharField(required=False, allow_blank=True)

    class Meta:
        model = StandfordUser
        fields = ['first_name', 'last_name', 'username', 'email' , 'password', 'student_id', 'department', 'role']

    def create(self, validated_data):
        # i want to collect/seperate data
        role = validated_data.pop('role')
        student_id = validated_data.pop('student_id', None)
        department = validated_data.pop('department', None)
        password = validated_data.pop('password')

        # creating a standford user account/ instance
        user = StandfordUser(**validated_data)
        user.is_admin = role == 'admin'
        user.is_student = role == 'student'
        user.set_password(password)
        user.save()

        # we want to identify if user is admin or student
        # we create either a student account or an admin

        if role == 'admin':
            Admin.objects.create(user=user, department=department)
        elif role == 'student':
            Student.objects.create(user=user, student_id=student_id)

        return user
        # {
        #     'username' : 'philip',
        #     'password' : 'luke456',
        #     'first_name' : 'philip',
        #     'last_name' : 'jude',
        #     'email' : 'philip@glimps.ru',
        #     'student_id': "",
        #     'department' : 'cybersecurity',
        #     'role' : 'admin'
        # }
