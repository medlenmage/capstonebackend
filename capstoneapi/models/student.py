from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from .paymenttype import PaymentType

class Student(models.model):
    
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING,)
    balance = models.IntegerField(validators=[MinValueValidator(0)],)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.DO_NOTHING)
    application_status = models.BooleanField(default=False)