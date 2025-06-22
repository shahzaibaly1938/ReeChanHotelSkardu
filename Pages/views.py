from django.shortcuts import render
from .models import Restaurant, Special_Dish, Dishe, Aboutus, Contactus, MeetingsPage, Home
from Accommodation.models import Room_type
# Create your views here.

def home(request):
    aboutus = Aboutus.objects.all().first()
    home = Home.objects.all().first()
    rooms = Room_type.objects.all()
    meeting = MeetingsPage.objects.all().first()
    restaurant = Restaurant.objects.all().first()

    context = {
        'aboutus':aboutus,
        'home':home,
        'rooms':rooms,
        'meeting':meeting,
        'restaurant':restaurant,
    }
    return render(request, 'pages/home.html', context)


def restaurant(request):
    restaurant = Restaurant.objects.all().first()
    specialdish = Special_Dish.objects.all()
    dishes = Dishe.objects.all()
    context = {
        'restaurant':restaurant,
        'special_dishes':specialdish,
        'dishes':dishes,
    }
    return render(request, 'pages/restaurant.html', context)


def contact(request):
    contactus = Contactus.objects.all().first()
    return render(request, 'pages/contact.html',{'contactus':contactus})

def event(request):
    meetingspage = MeetingsPage.objects.all().first()
    return render(request, 'pages/event.html',{'meetingspage':meetingspage})

def about(request):
    about = Aboutus.objects.all().first()
    return render(request, 'pages/about.html',{'about':about})

def reserve_table(request):
    return render(request, 'pages/reserve_table.html')