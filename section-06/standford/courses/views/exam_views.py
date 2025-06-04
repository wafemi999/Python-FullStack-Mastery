from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from courses.models.exam import Exam
from courses.serializers.exam_serializer import ExamSerializer
from rest_framework.generics import *
from rest_framework.permissions import AllowAny

class ExamListCreateView(ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [AllowAny]

class ExamDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


