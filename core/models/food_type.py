from django.db import models

class FoodType(models.Model):
    description = models.CharField(max_length=255)