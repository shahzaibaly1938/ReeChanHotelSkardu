from django.shortcuts import render
from .models import Room_type
# Create your views here.

def Accomodation(request):
    
    rooms = Room_type.objects.all()
    return render(request, "accomodation/accomodation.html", {'rooms':rooms})


def room_details(request, id):
    room = Room_type.objects.get(id=id)
    return render(request, 'accomodation/room-details.html', {'room':room})