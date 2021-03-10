from django.db import models

class CompanyContact(models.Model):

    company_name = models.CharField(max_length=30)
    contact_name = models.CharField(max_length=30)
    contact_phone_number = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=30)