from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('register/', views.register, name="registration-page"),
    path('verify/', views.verify, name="verification-page")
]