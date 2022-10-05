from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class Department(models.Model):
    dep_name = models.CharField(max_length=7)
    dep_head = models.CharField(max_length=100)
    dep_ID = models.CharField(max_length=20)

    def __str__(self):
        return self.dep_name


class Student(models.Model):
    gender = (
        ('Female','Female'),
        ('Male', 'Male')
    )
    levels = (
        (1 ,1),
        (2 ,2),
        (3 ,3),
        (4 ,4)
    )
    activity = (
        ('Active','Active'),
        ('Inactive', 'Inactive')
    )
   
    
    st_name = models.CharField(max_length=100)
    st_id = models.CharField(max_length=8)
    st_phone = models.CharField(max_length=15)
    st_email = models.EmailField(max_length=100)
    st_birthdate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    st_gender = models.CharField(max_length=6, choices=gender)
    st_level = models.IntegerField(choices=levels)
    st_active = models.CharField(max_length=8, choices=activity, default='Active')
    st_gpa = models.FloatField(null=True)
    department = models.ForeignKey(Department, null=True, default='General', on_delete = models.SET_NULL)

    def __str__(self):
        return self.st_name


