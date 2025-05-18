from django.http import HttpResponse, JsonResponse 
from django.shortcuts import get_object_or_404
from courses.models.course import Course
from courses.serializers.course_serializer import CourseSerializer

def course_list(request):
    # serialization
    courses = Course.objects.all()
    # response = { "courses" : list(courses.values()) }

    serializer = CourseSerializer(courses, many=True)
    return JsonResponse(serializer.data, safe=False)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    serializer = CourseSerializer(course)
    return JsonResponse(serializer.data)
