from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.api.serializers.recommendation_serializer import RecommendationSerializer
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.models.recommendation import Recommendation

class RecommendationViewSet(LoginRequiredModelViewSet):

    def list(self, request):
        queryset = Recommendation.objects.order_by('pk')
        serializer = RecommendationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RecommendationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Recommendation.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = RecommendationSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Recommendation.objects.get(pk=pk)
        except Recommendation.DoesNotExist:
            return Response(status=404)
        serializer = RecommendationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Recommendation.objects.get(pk=pk)
        except Recommendation.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
