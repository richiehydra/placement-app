from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.student import Student
from django.views import View

from store.models.company import Company
from store.models.applications import Application

class CheckOut(View):
    def post(self, request):
        profile = request.POST.get('profile')
        phone = request.POST.get('phone')
        student = request.session.get('student')
        cart = request.session.get('cart')
        companies = Company.get_companies_by_id(list(cart.keys()))

        for company in companies:
            print(cart.get(str(company.id)))
            order = Application(student=Student(id=student),
                          company=company,
                          cgpa=company.cgpa,
                          profile=profile,
                          phone=phone,
            )
            order.save()
        request.session['cart'] = {}

        return redirect('cart')