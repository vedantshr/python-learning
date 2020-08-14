from django.shortcuts import render
from django.http import HttpResponse
from .models import mobile

# Create your views here.

def index(request):
     return render(request, "index.html", {'delete':False})

def search(request):
    model_number_ip = request.POST.get('model_number', '')
    # deletetrue_ip = request.POST.get('deletetrue', '')

    try:
        query = mobile.objects.get(modelno_db=model_number_ip)
        mobileDetails = [query.modelno_db,query.price_db,query.year_db,query.company_db,query.RAM_db,query.ROM_db]
        return render(request, "single.html", {"data":mobileDetails, 'delete':False})
    
    except:
        return HttpResponse("Model number doesn't exist.")

def add(request):
    return render(request, "add.html")

def addentry(request):
    model_number_ip = request.POST.get('model_number', '')
    price_ip = request.POST.get('price', '')
    year_ip = request.POST.get('year', '')
    company_ip = request.POST.get('company', '')
    RAM_ip = request.POST.get('RAM', '')
    ROM_ip = request.POST.get('ROM', '')

    query = mobile(modelno_db=model_number_ip,price_db=price_ip,year_db=year_ip,company_db=company_ip,RAM_db=RAM_ip,ROM_db=ROM_ip)
    query.save()
    return render(request, "index.html")

def delete(request):
    return render(request, "index.html", {"delete":True})

def deletepage(request):
    model_number_ip = request.POST.get('model_number', '')

    try:
        query = mobile.objects.get(modelno_db=model_number_ip)
        mobileDetails = [query.modelno_db,query.price_db,query.year_db,query.company_db,query.RAM_db,query.ROM_db]
        return render(request, "single.html", {"data":mobileDetails, 'delete':True})
    
    except:
        return HttpResponse("Model number doesn't exist.")

def deleteentry(request):
    model_number_ip = request.POST.get('entry', '')

    try:
        query = mobile.objects.get(modelno_db=model_number_ip)
        query.delete() 
        return render(request, "index.html", {'delete':False})

    except:
        return HttpResponse("Model number doesn't exist.")

def viewall(request):
    try:
        dbObj = mobile.objects.all()
        dbData = [str(element) for element in list(dbObj)]
        finalData = [element.split("*") for element in dbData]

        return render(request, "viewall.html", {"data":finalData})

    except:
        return HttpResponse("No data exists.")
    
