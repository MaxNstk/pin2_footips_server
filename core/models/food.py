from django.db import models

class Food(models.Model):
    description = models.CharField(max_length=255, verbose_name='Descrição')
    calories = models.CharField(max_length=255, null=True, blank=True)
    serving_size = models.CharField(max_length=255, null=True, blank=True)
    total_fat = models.CharField(max_length=255, null=True, blank=True)
    saturated_fat = models.CharField(max_length=255, null=True, blank=True)
    cholesterol = models.CharField(max_length=255, null=True, blank=True)
    sodium = models.CharField(max_length=255, null=True, blank=True)
    carbohydrate = models.CharField(max_length=255, null=True, blank=True)
    proteins = models.CharField(max_length=255, null=True, blank=True)
    snack_type = models.IntegerField()
    food_type = models.ForeignKey('FoodType', on_delete=models.DO_NOTHING)