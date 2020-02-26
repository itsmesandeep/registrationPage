from django.db import models


# Create your models here.


class Employee_registraion_data(models.Model):
    emp_id = models.IntegerField(unique=True)
    emp_username = models.CharField(max_length=100,unique=True)
    emp_name = models.CharField(max_length=100)
    emp_age = models.IntegerField()
    emp_gender = models.CharField(max_length=100)
    emp_email = models.EmailField()
    emp_mobile = models.BigIntegerField()
    emp_password = models.CharField(max_length=100)
