from core.models.food_recomendation import FoodRecommendation
from django.db import models


class Recommendation(models.Model):
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    foods = models.ManyToManyField('Food', through=FoodRecommendation)
    content = models.TextField()