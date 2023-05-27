from rest_framework.serializers import ModelSerializer
from core.models import *

class RecommendationSerializer(ModelSerializer):

    class Meta:
        model = Recommendation
        fields = '__all__'