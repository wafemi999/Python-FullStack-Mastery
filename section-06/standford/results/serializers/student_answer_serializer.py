from rest_framework.serializers import ModelSerializer
from results.models.student_answer import StudentAnswer

class StudentAnswerSerializer(ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = '__all__'