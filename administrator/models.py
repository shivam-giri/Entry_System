# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model) :
    regNo = models.CharField(max_length=100, primary_key=True)
    fullName = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    fatherName = models.CharField(max_length=100)
    motherName = models.CharField(max_length=100)
    parentNumber = models.CharField(max_length=100)
    parentEmail = models.CharField(max_length=100)
    roomNo = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=100, blank=True)
    pic = models.ImageField(blank=True)
    def __str__(self):
        return self.fullName
    

    