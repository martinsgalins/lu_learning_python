from django.db import models


class StudentModel(models.Model):

    name = models.CharField(max_length=100)
    grades = models.CharField(max_length=4000)
    average_grade = models.FloatField()
