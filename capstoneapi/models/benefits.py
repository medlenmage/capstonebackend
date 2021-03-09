from django.db import models
from django.core.validators import MinValueValidator

class Benefits(models.Model):

    health_ins = models.CharField(max_length=30)
    dental_ins = models.CharField(max_length=30)
    life_ins = models.CharField(max_length=30)
    vacation_days = models.IntegerField(validators=[MinValueValidator(0)],)
    sick_days = models.IntegerField(validators=[MinValueValidator(0)],)
    