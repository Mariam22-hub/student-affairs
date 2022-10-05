
from django.contrib import admin
from django.urls import path, include
from re import template
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Table.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='templates/table&update/login.html'), name='login'),
]
