from rest_framework.serializers import *

class LoginSerializer(Serializer):
    username = CharField()
    email = CharField()
    role = CharField()
    password = CharField(write_only=True)

    