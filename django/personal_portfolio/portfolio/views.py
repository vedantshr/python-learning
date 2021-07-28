from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project


# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def about(request):
    return render(request, 'portfolio/about.html')

def projectdetail(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projectdetail.html', {'projects':projects})

# def forms(request):

#     return render(request, 'portfolio/forms.html')

def projectinfo(request, project_id):
    # projects = get_object_or_404(Project, pk=project_id)
    # # projects = Project.objects.all(project_id)
    # return render(request, 'portfolio/projectinfo.html', {'projects':projects})
    return render(request, 'portfolio/projectinfo.html')

