from rest_framework import viewsets
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.models import User
from rest_framework.response import Response

from core.api.serializers.user_serializer import UserSerializer

class UserViewSet(LoginRequiredModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)  