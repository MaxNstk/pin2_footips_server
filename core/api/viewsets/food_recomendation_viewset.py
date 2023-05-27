from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.api.serializers.food_recommendation_serializer import FoodRecommendationSerializer
from core.models.food_recomendation import FoodRecommendation


class FoodRecommendationViewSet(LoginRequiredModelViewSet):

    def list(self, request):
        queryset = FoodRecommendation.objects.order_by('pk')
        serializer = FoodRecommendationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = FoodRecommendationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = FoodRecommendation.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = FoodRecommendationSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = FoodRecommendation.objects.get(pk=pk)
        except FoodRecommendation.DoesNotExist:
            return Response(status=404)
        serializer = FoodRecommendationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = FoodRecommendation.objects.get(pk=pk)
        except FoodRecommendation.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)