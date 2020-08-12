from django.urls import path
from . import views

# URL definitions for the application. Has only two urls, the home page at 127.0.0.1:8000 (local host) and "process_form" for form submission.
urlpatterns = [
	path('', views.index, name='index'),
	path('demopage', views.demopage, name="demopage"),
	path('formpage', views.formpage, name="formpage"),
	path('formprocess', views.formprocess, name="formprocess")
]