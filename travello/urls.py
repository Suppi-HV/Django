from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pk>/', views.destination_detail, name='details'),
    path('comment/<int:comment_id>/<str:action>/', views.like_dislike_comment, name='like_dislike_comment'),
    

     # Ensure 'views.home' matches the function defined in views.py
]
