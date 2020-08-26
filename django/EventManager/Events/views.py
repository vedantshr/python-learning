from django.shortcuts import render
from django.http import HttpResponse
from .models import events

# Create your views here.

def index(request):
    return render(request, "index.html", {'delete':False}, {'edit':False})

def search(request):
    customer_name_ip = request.POST.get('customer_name', '')

    try:
        query = events.objects.get(customerName_db=customer_name_ip)
        eventsDetails = [query.name_db,query.place_db,query.month_db,query.year_db,query.startingPrice_db,query.maximumPrice,query.customerName_db]
        return render(request, "single.html", {"data":mobileDetails, 'delete':False})
    except:
        return HttpResponse("No such customer exists.")

def add(request):
    return render(request, "add.html")

def addentry(request):
    name_ip = request.POST.get('name', '')
    place_ip = request.POST.get('place', '')
    month_ip = request.POST.get('month', '')
    year_ip = request.POST.get('year', '')
    minimum_expenditure_ip = request.POST.get('minimum_expenditure', '')
    maximum_expenditure_ip = request.POST.get('maximum_expenditure', '')
    customer_name_ip = request.POST.get('customer_name', '')

    query = events(name_db=name_ip,place_db=place_ip,month_db=month_ip,year_db=year_ip,startingPrice_db=minimum_expenditure_ip,maximumPrice_db=maximum_expenditure_ip,customerName_db=customer_name_ip)
    query.save()
    return render(request, "index.html")

def delete(request):
    return render(request, "index.html", {"delete":True})

def deletepage(request):
    customer_name_ip = request.POST.get('customer_name', '')

    try:
        query = events.objects.get(customerName_db=customer_name_ip)
        mobileDetails = [query.name_db,query.place_db,query.month_db,query.year_db,query.startingPrice_db,query.maximumPrice_db,query.customerName_db]
        return render(request, "single.html", {"data":eventsDetails, 'delete':True})

    except:
        return HttpResponse("Customer doesn't exist.")

def deleteentry(request):
    customer_name_ip = request.POST.get('entry', '')

    try:
        query = events.objects.get(customerName_db=customer_name_ip)
        query.delete()
        return render(request, "single.html", {'delete':False})
    except:
        return HttpResponse("Customer doesn't exist.")

def viewall(request):
    try:
        dbObj = events.objects.all()
        dbData = [str(element) for element in list(dbObj)]
        finalData = [element.split("*") for element in dbData]

        return render(request, "viewall.html", {"data":finalData})

    except:
        return HttpResponse("No data exists.")

def edit(request):
    render(request, "index.html", {"edit":True})

def editpage(request):
    customer_name_ip = request.POST.get('customer_name', '')

    try:
        query = events.objects.get(customerName_db=customer_name_ip)
        eventsDetails = [query.name_db,query.place_db,query.month_db,query.year_db,query.startingPrice_db,query.maximumPrice_db,query.customerName_db]
        return render(request, "single.html", {"data":eventsDetails, 'edit':True})
    except:
        return HttpResponse("No change.")

def editentry(request):
    customer_name_ip = request.POST.get('customer_name', '')

    try:
        query = events.objects.get(customerName_db=customer_name_ip)
        query.customerName_db = customer_name_ip
        query.save()
        return render(request, "index.html", {'edit':False})
    except:
        return HttpResponse("Customer doesn't exist.")



