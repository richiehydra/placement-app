from django.db import models
from .company import Company
from .student import Student
import datetime


class Application(models.Model):
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE)
    student  = models.ForeignKey(Student,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cgpa= models.IntegerField()
    profile = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_applications_by_student(student_id):
        return Application.objects.filter(student=student_id).order_by('-date')