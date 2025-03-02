from django.db import  models
from django.core.validators import MinLengthValidator

class Student(models.Model):
    usn=models.IntegerField(default=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    cgpa=models.FloatField(default=0)

    def register(self):
        self.save()

    @staticmethod
    def get_Student_by_email(email):
        try:
            return Student.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Student.objects.filter(email = self.email):
            return True

        return  False
