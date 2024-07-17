from django.contrib import admin
from django.urls import path, include
from homepage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('thankyou', views.thank_you, name='thanks')
]