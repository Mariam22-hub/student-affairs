from django.urls import path
from . import views
from re import template
from django.urls import path 
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home1'),
    path('home/', views.homepage, name='home'),
    path('table/', views.students, name='data'),
    path('addrecord/', views.addrecord, name='add'),
    path('activity/', views.activity, name='activity'),
    path('update/<str:pk>/', views.updaterecord, name='update'),
    path('delete/<str:pk>/', views.deleterecord, name='delete'),
        path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


]