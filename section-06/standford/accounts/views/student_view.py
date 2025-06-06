from rest_framework.viewsets import ModelViewSet
from accounts.models.student import Student
from accounts.serializers.student_serializer import StudentSerializer
from accounts.permissions.isStudentOrReadOnly import IsAdminOrStudentOnly

class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrStudentOnly]
    http_method_names = ['get', 'list', 'put', 'patch', 'delete']


