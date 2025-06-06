from rest_framework.serializers import ModelSerializer
from results.models.exam_attempt import ExamAttempt

class ExamAttemptSerializer(ModelSerializer):
    class Meta:
        model = ExamAttempt
        fields = '__all__'