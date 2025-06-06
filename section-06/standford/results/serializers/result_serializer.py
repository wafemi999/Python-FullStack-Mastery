from rest_framework.serializers import ModelSerializer
from results.models.result import Result

class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'