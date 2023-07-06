from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Experience(request):
    return render(request,'Experience/experience.html')