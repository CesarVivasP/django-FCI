from django.shortcuts import render
from .models import Project

# Create your views here.

def cata(request):
    projects = Project.objects.all()
    return render(request, "cata/cata.html", {'projects' : projects})
