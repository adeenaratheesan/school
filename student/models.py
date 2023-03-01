from django.db import models

# Create your models here.
class Student(models.Model):
    
    student_name=models.CharField(max_length=50)
    age=models.BigIntegerField()
    gender=models.CharField(max_length=20)
    email=models.CharField(max_length=500)
    ph_number=models.CharField(max_length=20)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=16)
    
    class Meta:
        db_table='student'