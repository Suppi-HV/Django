from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    #path('details', views.details, name='details'),
    
     # Ensure 'views.home' matches the function defined in views.py
]
