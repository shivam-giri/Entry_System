# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Student
from student.models import Visit_Record
# Create your views here.
def admin_login(request):
    response = {}
    return render(request, 'administrator/index.html', response)

def verify_admin(request):
    response = {}
    if request.method == 'POST':
        response['error'] = "Invalid Credentials."
        user = authenticate(request, username=request.POST['uname'], password=request.POST['pswd'])
        if user:
            if user.is_superuser:
                login(request, user)
                return redirect('/administrator/home')
            else:
                return render(request, 'administrator/index.html', response)
        else:
            return render(request, 'administrator/index.html', response)
    return render(request, 'administrator/index.html', response)

@login_required(login_url='/administrator')
def home(request):
    response = {}
    return render(request, 'administrator/home.html', response)

@login_required(login_url='/administrator')
def regStudent(request):
    response = {}
    if request.method == "POST":
        std = Student()
        std.regNo = request.POST['regNo']
        std.fullName = request.POST['fullName']
        std.gender = request.POST['gender']
        std.roomNo = request.POST['roomNo']
        std.mobile = request.POST['mobile']
        std.course = request.POST['course']
        std.fatherName = request.POST['fatherName']
        std.motherName = request.POST['motherName']
        std.parentNumber = request.POST['parentNumber']
        std.parentEmail = request.POST['parentEmail']
        std.pic = request.FILES['pic']
        std.save()
        response['success'] = "Record Saved."
        return render(request, 'administrator/regStudent.html', response)
    return render(request, 'administrator/regStudent.html', response)

@login_required(login_url='/administrator')
def editStudent(request):
    response = {}
    if request.method == "POST":
        reg = request.POST['reg']
        std = Student.objects.get(regNo=reg)
        std.regNo = request.POST['regNo']
        std.fullName = request.POST['fullName']
        std.gender = request.POST['gender']
        std.roomNo = request.POST['roomNo']
        std.mobile = request.POST['mobile']
        std.course = request.POST['course']
        std.fatherName = request.POST['fatherName']
        std.motherName = request.POST['motherName']
        std.parentNumber = request.POST['parentNumber']
        std.parentEmail = request.POST['parentEmail']
        std.pic = request.FILES['pic']
        std.save()
        response['success'] = "Updated Successfully."
        return render(request, 'administrator/editStudent.html', response)
    return render(request, 'administrator/editStudent.html', response)

@login_required(login_url='/administrator')
def fetchStudent(request):
    response = {}
    if request.method == "POST":
        reg = request.POST['regNo']
        response['reg'] = reg
        try:
            std = Student.objects.get(regNo=reg)
            response['exist'] = True
            response['regNo'] = std.regNo
            response['fullName'] = std.fullName
            response['roomNo'] = std.roomNo
            response['mobile'] = std.mobile
            response['course'] = std.course
            response['fatherName'] = std.fatherName
            response['motherName'] = std.motherName
            if std.gender == "Male":
                response['male'] = std.gender
            if std.gender == "Female":
                response['female']  = std.gender
            response['pic'] = std.pic
            response['parentNumber'] = std.parentNumber
            response['parentEmail'] = std.parentEmail
            return render(request, 'administrator/editStudent.html', response)
        except Student.DoesNotExist:
            print("Invalid Registration Number.")
            response['error'] = "Invalid Registraton Number."
            return render(request, 'administrator/editStudent.html', response)
    return render(request, 'administrator/editStudent.html', response)
            
            
@login_required(login_url='/administrator')
def searchStudent(request):
    response = {}
    if request.method == "POST":
        reg = request.POST['regNo']
        try:
            std = Student.objects.get(regNo=reg)
            response['exist'] = True
            response['regNo'] = std.regNo
            response['fullName'] = std.fullName
            response['roomNo'] = std.roomNo
            response['mobile'] = std.mobile
            response['course'] = std.course
            response['fatherName'] = std.fatherName
            response['motherName'] = std.motherName
            response['gender'] = std.gender
            response['pic'] = std.pic
            response['parentNumber'] = std.parentNumber
            response['parentEmail'] = std.parentEmail
            response['visit_rec'] = Visit_Record.objects.filter(regNo=reg).order_by('-visitDate')
            return render(request, 'administrator/searchStudent.html', response)
        except Student.DoesNotExist:
            response['error'] = "Invalid Registration Number."
            return render(request, 'administrator/searchStudent.html', response)
    return render(request, 'administrator/searchStudent.html', response)

@login_required(login_url='/administrator')
def contactParent(request):
    response = {}
    if request.method == "POST":
        reg = request.POST['regNo']
        try:
            std = Student.objects.get(regNo=reg)
            response['exist'] = True
            response['regNo'] = std.regNo
            response['fullName'] = std.fullName
            response['roomNo'] = std.roomNo
            response['mobile'] = std.mobile
            response['course'] = std.course
            response['fatherName'] = std.fatherName
            response['motherName'] = std.motherName
            response['gender'] = std.gender
            response['pic'] = std.pic
            response['parentNumber'] = std.parentNumber
            response['parentEmail'] = std.parentEmail
            return render(request, 'administrator/contactParent.html', response)
        except Student.DoesNotExist:
            response['error'] = "Invalid Registration Number."
            return render(request, 'administrator/contactParent.html', response)
    return render(request, 'administrator/contactParent.html', response)


@login_required(login_url='/administrator')
def sendMail(request):
    response = {}
    if request.method == "POST":
        sub = request.POST['sub']
        msg = request.POST['msg']
        to_email = [request.POST['pEmail']]
        from_email = settings.EMAIL_HOST_USER
        send_mail (subject=sub, from_email=from_email, recipient_list=to_email, message=msg, fail_silently=False)
        response['success'] = "email send successfully."
        return render(request, 'administrator/contactParent.html', response)
    return render(request, 'administrator/contactParent.html', response)

def admin_logout(request):
    logout(request)
    return redirect("/administrator")