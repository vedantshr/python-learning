# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.index,name="home"),
    path('search',views.search,name="search"),
    path('add',views.add,name="add"),
    path('addentry',views.addentry,name="addentry"),
    path('delete',views.delete,name="delete"),
    path('deletepage',views.deletepage,name="deletepage"),
    path('deleteentry',views.deleteentry,name="deleteentry"),
    path('viewall',views.viewall,name="viewall"),
]