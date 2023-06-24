from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.api.serializers.food_type_serializer import FoodTypeSerializer
from core.models.food_type import FoodType

class FoodTypeViewSet(LoginRequiredModelViewSet):

    serializer_class = FoodTypeSerializer
    queryset = FoodType.objects.all()