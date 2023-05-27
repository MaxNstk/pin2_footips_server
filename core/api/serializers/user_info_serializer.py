from rest_framework.serializers import ModelSerializer
from core.models import *

class UserInfoSerializer(ModelSerializer):

    class Meta:
        model = UserInfo
        fields = '__all__'
