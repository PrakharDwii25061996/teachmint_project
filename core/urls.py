from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_form, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('liability/form/', views.liability_form, name='liability_form'),
    path('owe/form/', views.owe_form, name='owe_form')
    
]
