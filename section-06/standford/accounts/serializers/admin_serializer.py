from rest_framework.serializers import *
from accounts.serializers.user_serializer import UserSerializer

class AdminSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        fields = ['user', 'department']