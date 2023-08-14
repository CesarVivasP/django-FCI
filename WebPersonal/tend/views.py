from django.shortcuts import render
from .models import Project

# Create your views here.

def tend(request):
    projects = Project.objects.all()
    return render(request, "tend/tend.html", {'projects' : projects})