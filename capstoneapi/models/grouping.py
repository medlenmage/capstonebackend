from django.db.models.deletion import DO_NOTHING
from capstoneapi.models.employee import Employee
from django.db import models
from .employee import Employee
from .student import Student

class Grouping(models.Model):

    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name="groupings")
    instructor = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)