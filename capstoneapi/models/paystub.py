from safedelete import models as safe_delete_models
from django.db import models
from .directdeposit import DirectDeposit

class Paystub(safe_delete_models.SafeDeleteModel):

    _safedelete_policy = safe_delete_models.SOFT_DELETE
    salary = models.models.IntegerField(validators=[MinValueValidator(0)],)
    pay_period = models.DateField(default="0000-00-00",)
    deposit_date = models.DateField(default="0000-00-00",)
    deposit_account = models.models.ForeignKey(DirectDeposit, on_delete=models.DO_NOTHING)