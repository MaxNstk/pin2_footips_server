import json
from rest_framework import authentication, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, pagination
from django_filters.rest_framework import DjangoFilterBackend 


class CustomSearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        related_model = view.queryset.model._meta.get_fields()                          
        new_fields = [f'{field.attname}' for field in related_model if (
            field.concrete and field.attname != 'id' and field.__class__.__name__ != 'ForeignKey') 
        ]
        return new_fields

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
    
class LoginRequiredModelViewSet(ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [CustomSearchFilter, DjangoFilterBackend]
    pagination_class = StandardResultsSetPagination

    search_fields = '__all__'
    ordering_fields = '__all__'