from django.shortcuts import render, redirect
from .models import Restaurant, Special_Dish, Dishe, Aboutus, Contactus, MeetingsPage, Home, Table_Reservation, MeetingsnEvent
from Accommodation.models import Room_type
from django.contrib import messages
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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        datetime = request.POST.get('datetime')
        hours = request.POST.get('hours')
        info = request.POST.get('info')

        event_reservation = MeetingsnEvent(guest_name=name, email=email, address=address, phone_number=phone, 
                    datetime=datetime, reserved_for_hours=hours, additional_info=info   )
        event_reservation.save()
        messages.success(request, "Your event or meeting reservation request has been received. We will contact you shortly to confirm the details.")
        return redirect('home')

    meetingspage = MeetingsPage.objects.all().first()
    return render(request, 'pages/event.html',{'meetingspage':meetingspage})

def about(request):
    about = Aboutus.objects.all().first()
    return render(request, 'pages/about.html',{'about':about})

def reserve_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('contact')
        email = request.POST.get('email')
        datetime = request.POST.get('datetime')
        hours = request.POST.get('hours')
        info = request.POST.get('info')

        reservation = Table_Reservation(guest_name=name, phone_number=phone_number, datetime=datetime,
                     reserved_for_hours=hours, additional_info=info, email=email)
        reservation.save()
        messages.success(request, "Your table reservation request has been received successfully. We’ll be in touch shortly to confirm the details.")
        return redirect('home')

    return render(request, 'pages/reserve_table.html')


def privacy(request):
    return render(request, 'pages/privacy.html')