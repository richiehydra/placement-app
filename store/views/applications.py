from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.student import Student
from django.views import View

from store.models.company import Company
from store.models.applications import Application
from store.middlewares.auth import auth_middleware

class OrderView(View):

    def get(self , request ):
        student = request.session.get('student')
        applications = Application.get_applications_by_student(student)
        print(applications)
        return render(request , 'applications.html'  , {'applications' : applications})