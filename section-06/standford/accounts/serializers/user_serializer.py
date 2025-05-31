from rest_framework.serializers import *

class UserSerializer(ModelSerializer):
    class Meta:
        fields = ['id', 'first_name', 'last_name', 'username', 'email']