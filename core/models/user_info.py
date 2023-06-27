from django.db import models

class UserInfo(models.Model):
    heigth = models.FloatField()
    weight = models.FloatField()
    muscle_mass = models.FloatField()
    fat_percentage = models.FloatField()
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    imc = models.FloatField()

    def save(self, *args, **kwargs):
        if self.heigth and self.weight:
            self.imc = self.weight / (self.heigth*self.heigth)
        super().save(*args, **kwargs)


