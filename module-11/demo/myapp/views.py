"""
Author: Lane Dorscher
Date: 08/23/2026
Course: CSD-325
Assignment: 11.2
Description: Returns views from http request
"""

from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Dorscher says Hello!")