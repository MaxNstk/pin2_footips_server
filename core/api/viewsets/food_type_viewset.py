from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.api.serializers.food_type_serializer import FoodTypeSerializer
from core.models.food_type import FoodType

class FoodTypeViewSet(LoginRequiredModelViewSet):

    def list(self, request):
        queryset = FoodType.objects.order_by('pk')
        serializer = FoodTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = FoodTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = FoodType.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = FoodTypeSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = FoodType.objects.get(pk=pk)
        except FoodType.DoesNotExist:
            return Response(status=404)
        serializer = FoodTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = FoodType.objects.get(pk=pk)
        except FoodType.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

