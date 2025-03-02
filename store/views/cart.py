from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.student import Student
from django.views import View
from store.models.company import Company
from datetime import datetime

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        companies = Company.get_companies_by_id(ids)
        print(companies)
        return render(request, 'cart.html', {'companies': companies})
    
  
