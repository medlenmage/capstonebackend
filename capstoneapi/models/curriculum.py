from django.db import models

class Curriculum(models.Model):

    permit_lessons = models.CharField(max_length=50)
    driving_course = models.CharField(max_length=50)
    backing_course = models.CharField(max_length=50)
    pretrip_test = models.CharField(max_length=50)