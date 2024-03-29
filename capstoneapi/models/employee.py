from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from .benefits import Benefits

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,)
    benefits_id = models.ForeignKey(Benefits, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    