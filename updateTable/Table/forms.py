from dataclasses import field, fields
from logging import PlaceHolder
from tkinter import Widget
from django.forms import ModelForm, widgets
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
        
class UpdateForm(forms.ModelForm):

    # gen = (
    #     ('Female','Female'),
    #     ('Male', 'Male')
    # )

    
    # st_name = forms.CharField(label="Student's Name", max_length=100, widget=forms.TextInput(attrs= {
    #     'class' :'input',
    #     'placeholder' : 'ALex Martin',
    # }))

    # st_id = forms.CharField(label="Student's ID", max_length=8, widget=forms.TextInput(attrs= {
    #     'class' :'input',
    #     'placeholder' : '30200451',
    # }))

    # st_gpa = forms.FloatField(label="GPA", widget=forms.TextInput(attrs= {
    #     'class' :'input',
    #     'placeholder' : '3.5',
    # }))

    # st_level = forms.IntegerField(label="Student's Level", validators=[MinValueValidator(1), MaxValueValidator(4)], widget=forms.TextInput(attrs= {
    #     'class' :'input',
    #     'placeholder' : '3',
    # }))


    # st_phone = forms.CharField(max_length=15, label="Student's Phone", widget=forms.TextInput(attrs= {
    #     'class' :'input',
    #     'placeholder' : '011548763',
    # }))

    # st_gender = forms.CharField(max_length=15, label='Gender' , widget=forms.Select(choices=gen))
        

    # st_email = forms.EmailField(max_length=100, label="Student's Email" ,widget=forms.TextInput(attrs= {
    #     'class' :'input',
    #     'placeholder' : 'test@google.com',
         
    # }))


    class Meta:
        model = Student
        fields = '__all__'
        # ['st_name', 'st_gpa', 'st_phone', 'st_level', 'st_email', 'st_gender', 'st_name', 'st_id',
        # 'department', 'st_birthdate' ]