from rest_framework.serializers import *
from django.contrib.auth import authenticate

class LoginSerializer(Serializer):
    username = CharField()
    password = CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise ValidationError('Username or password is invalid')
        if not user.is_active:
            raise ValidationError('User is not active')
        data['user'] = user
        return data


        # {
        #     'username' : 'philip',
        #     'password' : 'luke456'
        #     'user' : {
        # }
        # }
        

        