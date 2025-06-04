# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from accounts.models.student import Student
from accounts.models.admin import Admin
from accounts.serializers.login_serializer import LoginSerializer
from accounts.serializers.user_serializer import UserSerializer

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            role = 'admin' if user.is_admin else 'student'
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': UserSerializer(user).data,
                'role': role
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        #  deleting user auth token
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
