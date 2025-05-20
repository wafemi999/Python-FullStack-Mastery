from rest_framework.serializers import ModelSerializer
from questions.models.exam_question import ExamQuestion

class ExamQuestionSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ExamQuestion