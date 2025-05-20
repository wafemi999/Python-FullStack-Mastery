from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from django.shortcuts import get_object_or_404
from questions.models.exam_choice import ExamChoice
from questions.serializers.exam_choice_serializer  import ExamChoiceSerializer

class ExamChoiceListCreateView(APIView):
    """ This view is going to return all exam choices in the course model """

    def get(self, request, format=None):
        courses = ExamChoice.objects.all()
        serializer =  ExamChoiceSerializer(courses, many=True)
        return Response(serializer.data, HTTP_200_OK)

    def post(self, request):
        serializer = ExamChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ExamChoiceDetailUpdateDeleteView(APIView):

    def get(self, request, pk):
        course = get_object_or_404(ExamChoice, pk=pk)
        serializer = ExamChoiceSerializer(course)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, pk):
        course = get_object_or_404(ExamChoice, pk=pk)
        serializer = ExamChoiceSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = get_object_or_404(ExamChoice, pk=pk)
        course.delete()
        return Response({"status" : "Exam Choice deleted sucessfully"}, status=HTTP_204_NO_CONTENT)


# List Create Update Delete -> CRUD