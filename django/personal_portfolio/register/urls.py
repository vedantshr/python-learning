from django.contrib import admin 
from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.register, name="register"),
]
