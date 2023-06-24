import json
from rest_framework import authentication, permissions
from rest_framework.viewsets import ViewSet


class LoginRequiredModelViewSet(ViewSet):
    authentication_classes = (authentication.SessionAuthentication,authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    filterset_fields = '__all__'