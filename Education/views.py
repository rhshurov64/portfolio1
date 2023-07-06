from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Education(request):
    return render(request,'Education/education.html')