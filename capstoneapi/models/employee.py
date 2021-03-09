from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from .benefits import Benefits
from .companycontact import CompanyContact
from .directdeposit import DirectDeposit

class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING,)
    paystub_id = models.ForeignKey(Paystub, on_delete=models.DO_NOTHING,)
    benefits_id = models.ForeignKey(Benefits, on_delete=models.DO_NOTHING,)
    companycontact_id = models.ForeignKey(CompanyContact, on_delete=models.DO_NOTHING)
    deposit_account = models.ForeignKey(DirectDeposit, on_delete=models.DO_NOTHING)
    is_admin = models.BooleanField(default=False)
    