from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_name=models.CharField(max_length=150)
    emp_con=models.CharField(max_length=15)
    emp_salary=models.FloatField()
