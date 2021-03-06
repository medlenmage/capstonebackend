from django.db import models
from safedelete.models import SafeDeleteModel
from django.core.validators import MinValueValidator
from safedelete.models import SOFT_DELETE

class PaymentType(SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE
    account_number = models.IntegerField(validators=[MinValueValidator(0)],)
    routing_number = models.IntegerField(validators=[MinValueValidator(0)],)
    bank_name = models.CharField(max_length=25)
    payment_name = models.CharField(max_length=25)