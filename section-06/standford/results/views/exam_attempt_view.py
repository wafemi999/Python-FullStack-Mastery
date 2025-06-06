from rest_framework.viewsets import ModelViewSet
from results.serializers.exam_attempt_serializer import ExamAttemptSerializer
from results.models.exam_attempt import ExamAttempt


class ExamAttemptViewSet(ModelViewSet):
    queryset = ExamAttempt.objects.all()
    serializer_class = ExamAttemptSerializer

