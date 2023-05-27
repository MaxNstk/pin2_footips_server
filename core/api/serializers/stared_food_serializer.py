from rest_framework.serializers import ModelSerializer
from core.models import *

class StaredFoodSerializer(ModelSerializer):

    class Meta:
        model = StaredFood
        fields = '__all__'