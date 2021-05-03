from django.db.models.deletion import DO_NOTHING
from capstoneapi.models.employee import Employee
from django.db import models
from .employee import Employee
from .student import Student

class Grouping(models.Model):

    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    instructor = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()