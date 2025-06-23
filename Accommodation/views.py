from django.shortcuts import render, redirect
from .models import Room_type, Booking
from django.contrib import messages
# Create your views here.

def Accomodation(request):
    
    rooms = Room_type.objects.all()
    return render(request, "accomodation/accomodation.html", {'rooms':rooms})


def room_details(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        room_type = request.POST.get('room_type')
        total_rooms = request.POST.get('total_rooms')
        adults = request.POST.get('no_of_adults')
        children = request.POST.get('total_children')
        phone_number = request.POST.get('number')
        email = request.POST.get('email')

        booking = Booking(name=name, check_in=checkin, check_out=checkout, 
                room_type=Room_type.objects.get(id=room_type), no_of_rooms=total_rooms,
                adults=adults, children=children, phone_number=phone_number, email=email)
        booking.save()
        messages.success(request, "Your reservation inquiry has been received successfully. We will contact you shortly to confirm the details.")
        return redirect('home')


    room = Room_type.objects.get(id=id)
    room_types = Room_type.objects.all()
    return render(request, 'accomodation/room-details.html', {'room':room, 'room_types':room_types})