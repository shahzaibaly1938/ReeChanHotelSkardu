from django.urls import path
from . import views

urlpatterns = [
    path('', views.Accomodation, name='Accomodation'),
]
