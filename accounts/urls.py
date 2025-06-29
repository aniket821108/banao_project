# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('about-us/', views.aboutUS, name='aboutus'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
     path('logout/', views.user_logout, name='logout'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]
