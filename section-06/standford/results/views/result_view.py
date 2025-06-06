from rest_framework.viewsets import ModelViewSet
from results.models.result import Result
from results.serializers.result_serializer import ResultSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ResultViewSet(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    filterset_fields = ['score']
    filter_backends = [DjangoFilterBackend]
