from django.db import models

class UserInfo(models.Model):
    heigth = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    muscle_mass = models.FloatField(default=0)
    fat_percentage = models.FloatField(default=0)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    imc = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        try:
            if self.heigth and self.weight:
                self.imc = self.heigth / (self.weight*self.weight)
        except: pass
        
        super().save(*args, **kwargs)


