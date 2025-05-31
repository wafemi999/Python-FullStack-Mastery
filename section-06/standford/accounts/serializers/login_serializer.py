from rest_framework.serializers import *
from django.contrib.auth import authenticate

class LoginSerializer(Serializer):
    username = CharField()
    password = CharField(write_only=True)

    def validate(self, data):
        user = authenticate(data['username'], data['password'])
        if user:
            return "Login successfullly"
        else:
            return  "Password or username or both are invalid"
        
        