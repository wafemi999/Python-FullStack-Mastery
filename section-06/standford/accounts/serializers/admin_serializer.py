from rest_framework.serializers import *
from accounts.models.admin import Admin
from accounts.serializers.user_serializer import UserSerializer

class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = ['user', 'department']