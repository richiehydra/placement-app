from django.contrib import admin
from .models.company import Company
from .models.category import Category
from .models.student import Student
from .models.applications import Application


class AdminCompany(admin.ModelAdmin):
    list_display = ['name', 'cgpa', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Company, AdminCompany)
admin.site.register(Category, AdminCategory)
admin.site.register(Student)
admin.site.register(Application)
