from rest_framework.serializers import ModelSerializer
from core.models import *

class FoodRecommendationSerializer(ModelSerializer):

    class Meta:
        model = FoodRecommendation
        fields = '__all__'
