from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from .benefits import Benefits

from .directdeposit import DirectDeposit

class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING,)
    benefits_id = models.ForeignKey(Benefits, on_delete=models.DO_NOTHING, blank=True, null=True)
    deposit_account = models.ForeignKey(DirectDeposit, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    