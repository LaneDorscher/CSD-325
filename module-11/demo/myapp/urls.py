"""
Author: Lane Dorscher
Date: 08/23/2026
Course: CSD-325
Assignment: 11.2
Description: Handles configuring url routes to resources within the myapp project
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]
