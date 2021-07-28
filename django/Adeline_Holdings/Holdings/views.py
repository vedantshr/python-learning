from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def projectdetail(request):
    projects = Project.objects.all()
    return render(request, 'projectdetail.html', {'projects':projects})

def projectinfo(request):
    return render(request, 'projectinfo.html')