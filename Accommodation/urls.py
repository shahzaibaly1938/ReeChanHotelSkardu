from django.urls import path
from . import views

urlpatterns = [
    path('', views.Accomodation, name='Accomodation'),
    path('room-details/', views.room_details, name='room-details'),
]
