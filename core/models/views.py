from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from core.serializers import UserSerializer, FoodSerializer, FoodRecommendationSerializer, RecommendationSerializer, StaredFoodSerializer, FoodTypeSerializer, UserInfoSerializer
from core.models import User, Food, FoodRecommendation, Recommendation, StaredFood, FoodType, UserInfo



