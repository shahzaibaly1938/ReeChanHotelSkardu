from django.shortcuts import render

# Create your views here.

def Accomodation(request):
    return render(request, "accomodation/accomodation.html")


def room_details(request):
    return render(request, 'accomodation/room-details.html')