from django.db import models

class FoodRecommendation(models.Model):
    food = models.ForeignKey('Food', on_delete=models.DO_NOTHING)
    recommendation = models.ForeignKey('Recommendation', on_delete=models.DO_NOTHING)