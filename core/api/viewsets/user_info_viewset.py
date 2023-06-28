from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.api.serializers.user_info_serializer import UserInfoSerializer
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.models.user_info import UserInfo

class UserInfoViewSet(LoginRequiredModelViewSet):

    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()

    def list(self, request, *args, **kwargs):
        user_info, created = UserInfo.objects.get_or_create(user = request.user)
        serializer = self.get_serializer(user_info)
        return Response(serializer.data)    