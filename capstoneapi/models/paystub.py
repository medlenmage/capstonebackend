from safedelete import models as safe_delete_models
from django.db import models
from django.core.validators import MinValueValidator
from .directdeposit import DirectDeposit
from .employee import Employee

class Paystub(safe_delete_models.SafeDeleteModel):

    _safedelete_policy = safe_delete_models.SOFT_DELETE
    employee_id = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    salary = models.IntegerField(validators=[MinValueValidator(0)],)
    pay_period = models.DateField(default="0000-00-00",)
    deposit_date = models.DateField(default="0000-00-00",)
    deposit_account = models.ForeignKey(DirectDeposit, on_delete=models.DO_NOTHING)