# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from administrator.models import Student
# Create your models here.
class Visit_Record(models.Model):
    regNo = models.ForeignKey(Student, null=False, on_delete=models.CASCADE)
    goingTo = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)
    visitDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.goingTo