from django.urls import path
from django.conf.urls import include, url
#url
from . import views
# from .views import SearchResults

urlpatterns = [
    path('', views.index, name ='index'),
    path('LoginForm.html', views.LoginForm, name ='LoginForm'),
    path('dashboard.html', views.dashboard, name ='dashboard'),
    path('register.html', views.register, name ='register'),
    path('modList.html', views.modList, name = 'modList'),
    path('<int:mod_id>/', views.modDetails, name = 'details'),
    path('About.html', views.About, name = 'about'),
    path('search.html', views.search, name='search'),
    path('gameList.html', views.gameList, name='modList'),
    path('publish.html', views.publish, name='publish'),
    path('boards.html', views.boards, name='boards'),
    path('boards/<int:dis_id>/',views.discussion, name='discussion'),
]