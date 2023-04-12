from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    heigth = models.FloatField()
    weight = models.FloatField()
    imc = models.FloatField()
