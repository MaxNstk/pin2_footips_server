from rest_framework.serializers import ModelSerializer
from core.models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'birth_date')
