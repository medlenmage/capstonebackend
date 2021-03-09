from django.contrib.auth.models import Group
from django.db import models
from django.db.models.deletion import DO_NOTHING
from .employee import Employee
from .grouping import Grouping
from .equipment import Equipment
from .curriculum import Curriculum

class School(models.Model):

    employee_id = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    grouping_id = models.ForeignKey(Grouping, on_delete=models.DO_NOTHING)
    equipment_id = models.ForeignKey(Equipment, on_delete=models.DO_NOTHING)
    curriculum_id = models.ForeignKey(Curriculum, on_delete=models.DO_NOTHING)