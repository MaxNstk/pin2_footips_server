

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.api.serializers.food_serializer import FoodSerializer
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.models.food import Food

class FoodViewSet(LoginRequiredModelViewSet):

    def list(self, request):
        queryset = Food.objects.order_by('pk')
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Food.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = FoodSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Food.objects.get(pk=pk)
        except Food.DoesNotExist:
            return Response(status=404)
        serializer = FoodSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Food.objects.get(pk=pk)
        except Food.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
