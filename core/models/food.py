from django.db import models

class Food(models.Model):
    description = models.CharField(max_length=255, verbose_name='Descrição')
    calories = models.FloatField()
    lipids = models.FloatField()
    carbohydrate = models.FloatField()
    proteins = models.FloatField()
    snack_type = models.IntegerField()