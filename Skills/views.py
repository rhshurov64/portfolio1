from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Skills(request):
    return render(request,'Skills/skills.html')