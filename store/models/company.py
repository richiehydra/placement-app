from django.db import models
from .category import Category


class Company(models.Model):
    name = models.CharField(max_length=50)
    cgpa= models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_companies_by_id(ids):
        return Company.objects.filter(id__in =ids)

    @staticmethod
    def get_all_companies():
        return Company.objects.all()

    @staticmethod
    def get_all_companies_by_categoryid(category_id):
        if category_id:
            return Company.objects.filter(category = category_id)
        else:
            return Company.get_all_companies()