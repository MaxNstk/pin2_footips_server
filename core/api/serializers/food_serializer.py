from rest_framework.serializers import ModelSerializer
from core.models import *
from rest_framework.serializers import SerializerMethodField

class FoodSerializer(ModelSerializer):
    is_stared = SerializerMethodField()

    class Meta:
        model = Food
        fields = '__all__'

    def get_is_stared(self, instance):
        return StaredFood.objects.filter(food=instance, user=self.context['request'].user).exists()