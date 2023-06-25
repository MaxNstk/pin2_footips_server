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
