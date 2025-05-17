from rest_framework.serializers import *
from courses.models.exam import Exam

class ExamSerializer(Serializer):
    course_id = IntegerField()
    title = CharField(max_length=50)
    total_marks = IntegerField()
    date = DateTimeField()
    duration_minutes = IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Exam` instance, given the validated data.
        """
        return Exam.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Exam` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.total_marks = validated_data.get('total_marks', instance.total_marks)
        instance.date = validated_data.get('date', instance.date)
        instance.duration_minutes = validated_data.get('duration_minutes', instance.duration_minutes)
        instance.save()
        return instance