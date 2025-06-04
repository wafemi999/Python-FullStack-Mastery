from rest_framework.viewsets import ModelViewSet
from accounts.models.admin import Admin
from accounts.serializers.admin_serializer import AdminSerializer
from rest_framework.permissions import IsAdminUser

class AdminsViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['get', 'list', 'put', 'patch', 'delete']

