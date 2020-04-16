from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='retard-home'),
    path('refresh', views.refresh, name='retard-refresh'),
]
