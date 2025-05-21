from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from courses.models.exam import Exam
from courses.serializers.exam_serializer import ExamSerializer
from django.shortcuts import get_object_or_404


class ExamListCreateView(APIView):

    def get(self, request, format=None):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True, context={"request": request})
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = ExamSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ExamDetailUpdateDeleteView(APIView):
    def get(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk)
        serializer = ExamSerializer(exam, context={"request": request})
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk)
        serializer = ExamSerializer(exam, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk)
        exam.delete()
        return Response({"status": "Exam deleted successfully"}, status=HTTP_204_NO_CONTENT)

