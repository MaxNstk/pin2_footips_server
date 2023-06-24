from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.api.serializers.recommendation_serializer import RecommendationSerializer
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.models.recommendation import Recommendation

class RecommendationViewSet(LoginRequiredModelViewSet):

    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all()