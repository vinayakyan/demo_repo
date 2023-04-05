from django.db import models


class Student(models.Model):
    roll = models.PositiveIntegerField()
    name = models.CharField(max_length=20, db_comment="Name of Student")
    marks = models.FloatField()

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'

