from capstoneapi.models.employee import Employee
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
from django.core.validators import MinValueValidator
from .employee import Employee

class DirectDeposit(SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE
    account_number = models.IntegerField(validators=[MinValueValidator(0)],)
    routing_number = models.IntegerField(validators=[MinValueValidator(0)],)
    bank_name = models.CharField(max_length=25)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name="direct_deposit",blank=True, null=True)
    account_name = models.CharField(max_length=25)