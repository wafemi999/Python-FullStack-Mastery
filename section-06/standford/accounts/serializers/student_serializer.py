from rest_framework.serializers import *
from accounts.serializers.user_serializer import UserSerializer

class StudentSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        fields = ['user', 'student_id']