from django.db import models

class StaredFood(models.Model):
    food = models.ForeignKey('Food', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
