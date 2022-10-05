from django.shortcuts import render, redirect 
from .models import * 
from .forms import UpdateForm
from .filters import StudentFilter
from .filters import StatusFilter

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm

def login(request):
    return render(request, 'table&update/login.html')


def logout(request):
    return render(request, 'table&update/logout.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hello {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'table&update/register.html', {'form':form})

def profile(request):
    return render(request, 'table&update/profile.html')
   




StatusFilter
def activity(request):
    studs = Student.objects.all()
    
    myFilter2 = StatusFilter(request.GET, queryset=studs)
    studs = myFilter2.qs
    
    context = {'studs':studs, 'myFilter':myFilter2}
    return render (request, 'table&update/activity.html', context)

def home(request):
    return render (request, 'table&update/Home1.html')

def homepage(request):
    return render (request, 'table&update/HomePage.html')

def students(request):
    studs = Student.objects.all()
    
    myFilter = StudentFilter(request.GET, queryset=studs)
    studs = myFilter.qs
    
    context = {'studs':studs, 'myFilter':myFilter}
    return render (request, 'table&update/tables.html', context)

def deleterecord(request, pk):
    stu = Student.objects.get(id = pk)
    if request.method == 'POST':
        stu.delete()
        return redirect('/')
    context = {'form' : stu}
    return render(request, 'table&update/delete.html', context)
    

def updaterecord(request, pk):
    stu = Student.objects.get(id = pk)
    form = UpdateForm(instance = stu)
    
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance = stu)

        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form' : form}
    return render (request, 'table&update/update.html', context)

    
    
def addrecord(request):
    form = UpdateForm()

    if request.method == 'POST':
        form = UpdateForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}
    return render (request, 'table&update/update.html', context)
    
 