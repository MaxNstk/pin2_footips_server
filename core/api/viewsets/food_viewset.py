from core.api.serializers.food_serializer import FoodSerializer
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.models.food import Food

class FoodViewSet(LoginRequiredModelViewSet):

    serializer_class = FoodSerializer
    queryset = Food.objects.all()

