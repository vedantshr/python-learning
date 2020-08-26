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
    path('viewall',views.viewall,name="viewall"),
    path('edit',views.edit,name="edit"),
    path('editpage',views.editpage,name="editpage"),
    path('editentry',views.editentry,name="editentry"),
]
