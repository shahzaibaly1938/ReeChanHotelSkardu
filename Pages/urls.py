from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('contact/', views.contact, name='contact'),
    path('events&meetings/', views.event, name='event'),
    path('aboutus/', views.about, name='about'),
    path('reserve-table/', views.reserve_table, name='reserve_table'),
]