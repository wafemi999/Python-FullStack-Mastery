from rest_framework.serializers import ModelSerializer, SerializerMethodField
from questions.models.exam_question import ExamQuestion

class ExamQuestionSerializer(ModelSerializer):
    no_of_choices = SerializerMethodField()
    class Meta:
        fields = '__all__'
        model = ExamQuestion

    def get_no_of_choices(self, obj):
        return obj.examchoice_set.count()