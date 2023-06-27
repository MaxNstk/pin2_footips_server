from django.db import models

class Food(models.Model):
    description = models.CharField(max_length=255, verbose_name='Descrição')
    calories = models.FloatField(null=True, blank=True)
    serving_size = models.FloatField(null=True, blank=True)
    total_fat = models.FloatField(null=True, blank=True)
    saturated_fat = models.FloatField(null=True, blank=True)
    cholesterol = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    carbohydrate = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    food_type = models.ForeignKey('FoodType', on_delete=models.DO_NOTHING)