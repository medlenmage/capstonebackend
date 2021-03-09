from django.db import models

class Equipment(models.model):

    equipment_type = models.CharField(max_length=30)
    is_available = models.BooleanField(default=True)