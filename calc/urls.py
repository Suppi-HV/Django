from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('add',views.add,name= 'add') # Ensure 'views.home' matches the function defined in views.py
]
