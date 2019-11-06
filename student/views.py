# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Student, Visit_Record
# Create your views here.
def EnterReg(request):
    response = {}
    print("Enter Registration")
    return render(request, 'student/index.html', response)

def fetchDetails(request):
    response = {}
    if request.method == "POST":
        reg = request.POST['regNo']
        try:
            std = Student.objects.get(regNo=reg)
            response['regNo'] = reg
            response['name'] = std.fullName
            response['course'] = std.course
            response['fname'] = std.fatherName
            response['mname'] = std.motherName
            response['img'] = std.pic
            return render(request, 'student/enterDetails.html', response)
        except Student.DoesNotExist:
            response['error'] = "Invalid Registration Number."
            return render(request, 'student/index.html', response)
    return render(request, 'student/enterDetails.html', response)

def saveDetails(request):
    response = {}
    if request.method == "POST":
        std = Student.objects.get(regNo=request.POST['regNo'])
        record = Visit_Record()
        record.regNo = std
        record.goingTo = request.POST['goingTo']
        record.purpose = request.POST['purpose']
        record.save()
        response["success"] = "Recored Saved Successfully."
        print("Visit Record Saved.")
        return render(request, 'student/index.html', response)
    return render(request, 'student/enterDetails.html', response)
