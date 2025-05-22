from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from courses.models.exam import Exam
from courses.serializers.exam_serializer import ExamSerializer
from rest_framework.generics import *

class ExamListCreateView(ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


