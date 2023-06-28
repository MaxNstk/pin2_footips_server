from core.api.serializers.food_serializer import FoodSerializer
from core.api.serializers.stared_food_serializer import StaredFoodSerializer
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.models.food import Food
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from core.models.stared_food import StaredFood


class FoodViewSet(LoginRequiredModelViewSet):

    serializer_class = FoodSerializer
    queryset = Food.objects.all()

    @action(detail=False, methods=['post'])
    def star(self,request,*args, **kwargs):
        food_id = request.data.get('food_id')
        food, created = StaredFood.objects.get_or_create(food_id=food_id, user=request.user)
        response = StaredFoodSerializer(food).data
        if not created:
            food.delete()
            return Response('deleted',status.HTTP_200_OK)
        return Response(response,status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        if request.GET.get('hypertrophy'):
            queryset = queryset.order_by('-protein')
        elif request.GET.get('slimming'):
            queryset = queryset.order_by('calories')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

