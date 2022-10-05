import django_filters
from django_filters import DateFilter

from .models import *

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = '__all__' 
        exclude = ['st_name', 'st_email', 'st_birthdate', 'st_gender', 'st_gpa', 'st_active']
        
class StatusFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = '__all__' 
        exclude = ['st_name', 'st_email', 'st_birthdate', 'st_gender', 'st_gpa', 'st_gender', 'st_id', 'st_phone', 'department', 'st_level']