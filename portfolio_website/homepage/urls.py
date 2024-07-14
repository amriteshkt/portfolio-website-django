from django.contrib import admin
from django.urls import path, include
from homepage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='project'),
    path('contactme/', views.contact_me, name='contact_me')
]