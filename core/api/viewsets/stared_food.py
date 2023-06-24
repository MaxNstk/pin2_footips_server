from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.api.serializers.stared_food_serializer import StaredFoodSerializer
from core.models.stared_food import StaredFood


class StaredFoodViewSet(LoginRequiredModelViewSet):

    serializer_class = StaredFoodSerializer
    queryset = StaredFood.objects.all()