from django.urls import path
from django.conf.urls import include
#url
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('LoginForm.html', views.LoginForm, name ='LoginForm'),
    path('dashboard.html', views.dashboard, name ='dashboard'),
    path('register.html', views.register, name ='register'),
    path('modList.html', views.modList, name = 'modList'),
    path('<int:mod_id>/', views.modDetails, name = 'details'),
    path('About.html', views.About, name = 'about')

]