from django.urls import path
from . import views

urlpatterns = [
    path('', views.Accomodation, name='Accomodation'),
    path('room-details/<int:id>/', views.room_details, name='room-details'),
]
