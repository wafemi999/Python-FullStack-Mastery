from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from django.shortcuts import get_object_or_404
from questions.models.exam_question import ExamQuestion
from questions.serializers.exam_question_serializer import ExamQuestionSerializer


class ExamQuestionListCreateView(APIView):

    def get(self, request, format=None):
        exams_questions = ExamQuestion.objects.all()
        serializer = ExamQuestionSerializer(exams_questions, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = ExamQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ExamQuestionDetailUpdateDeleteView(APIView):
    def get(self, request, pk):
        course = get_object_or_404(ExamQuestion, pk=pk)
        serializer = ExamQuestionSerializer(course)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, pk):
        course = get_object_or_404(ExamQuestion, pk=pk)
        serializer = ExamQuestionSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = get_object_or_404(ExamQuestion, pk=pk)
        course.delete()
        return Response({"status" : "Exam question deleted sucessfully"}, status=HTTP_204_NO_CONTENT)
