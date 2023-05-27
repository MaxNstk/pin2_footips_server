"""
URL configuration for foodtips project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework import routers


from rest_framework.routers import SimpleRouter
from core.api.viewsets.food_recomendation_viewset import FoodRecommendationViewSet
from core.api.viewsets.food_viewset import FoodViewSet
from core.api.viewsets.food_type_viewset import FoodTypeViewSet
from core.api.viewsets.recommendation_viewset import RecommendationViewSet
from core.api.viewsets.stared_food import StaredFoodViewSet
from core.api.viewsets.user_info_viewset import UserInfoViewSet

router = SimpleRouter()

router.register(r'food', FoodViewSet, 'Food')
router.register(r'foodrecommendation', FoodRecommendationViewSet, 'FoodRecommendation')
router.register(r'recommendation', RecommendationViewSet, 'Recommendation')
router.register(r'staredfood', StaredFoodViewSet, 'StaredFood')
router.register(r'foodtype', FoodTypeViewSet, 'FoodType')
router.register(r'userinfo', UserInfoViewSet, 'UserInfo')
# router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]
