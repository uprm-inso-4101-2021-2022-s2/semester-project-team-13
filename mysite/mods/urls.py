from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('LoginForm.html', views.LoginForm, name ='LoginForm'),
    path('dashboard.html', views.dashboard, name ='dashboard'),
    path('register.html', views.register, name ='register'),

]