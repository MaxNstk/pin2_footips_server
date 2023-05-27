from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.api.serializers.stared_food_serializer import StaredFoodSerializer
from core.models.stared_food import StaredFood


class StaredFoodViewSet(LoginRequiredModelViewSet):

    def list(self, request):
        queryset = StaredFood.objects.order_by('pk')
        serializer = StaredFoodSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StaredFoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = StaredFood.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = StaredFoodSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = StaredFood.objects.get(pk=pk)
        except StaredFood.DoesNotExist:
            return Response(status=404)
        serializer = StaredFoodSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = StaredFood.objects.get(pk=pk)
        except StaredFood.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)