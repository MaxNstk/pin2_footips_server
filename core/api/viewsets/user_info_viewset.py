from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.api.serializers.user_info_serializer import UserInfoSerializer
from core.api.viewsets.login_required_modelviewset import LoginRequiredModelViewSet
from core.models.user_info import UserInfo

class UserInfoViewSet(LoginRequiredModelViewSet):

    def list(self, request):
        queryset = UserInfo.objects.order_by('pk')
        serializer = UserInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = UserInfo.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserInfoSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = UserInfo.objects.get(pk=pk)
        except UserInfo.DoesNotExist:
            return Response(status=404)
        serializer = UserInfoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = UserInfo.objects.get(pk=pk)
        except UserInfo.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
