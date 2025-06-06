from rest_framework.viewsets import ModelViewSet
from results.models.student_answer import StudentAnswer
from results.serializers.student_answer_serializer import StudentAnswerSerializer

class StudentAnswerViewSet(ModelViewSet):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer
    

