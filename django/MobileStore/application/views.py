from django.shortcuts import render
from django.http import HttpResponse
from .models import userdetails
# Create your views here.

def index(request):
    return render(request, "index.html", {"form":False})

def demopage(request):
    return HttpResponse("This is my demopage.")

def formpage(request):
    return render(request, "index.html", {"form":True})

def formprocess(request):
    username_ip = request.POST.get('username', '')
    location_ip = request.POST.get('location', '')

    try:
        query = userdetails.objects.get(username_db=username_ip)
        if query.location_db != location_ip:
            query = userdetails(username_db = username_ip, location_db = location_ip)
            query.save()
        else:
            return HttpResponse("User data already exists.")
            
    except:
        query = userdetails(username_db = username_ip, location_db = location_ip)
        query.save()

    try:
        dbObj = userdetails.objects.all()
        dbData = [str(element) for element in list(dbObj)]
        finalData = [element.split("*") for element in dbData]

        return render(request, "display.html", {"data":finalData})

    except:
        return render(request, "display.html", {"data":None})