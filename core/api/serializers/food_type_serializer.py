from rest_framework.serializers import ModelSerializer
from core.models import *

class FoodTypeSerializer(ModelSerializer):

    class Meta:
        model = FoodType
        fields = '__all__'