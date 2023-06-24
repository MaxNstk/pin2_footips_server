from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.api.serializers.food_recommendation_serializer import FoodRecommendationSerializer
from core.models.food_recomendation import FoodRecommendation


class FoodRecommendationViewSet(LoginRequiredModelViewSet):

    serializer_class = FoodRecommendationSerializer
    queryset = FoodRecommendation.objects.all()