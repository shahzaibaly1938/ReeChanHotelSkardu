from django.shortcuts import render

# Create your views here.

def restaurant(request):
    return render(request, 'pages/restaurant.html')


def contact(request):
    return render(request, 'pages/contact.html')

def event(request):
    return render(request, 'pages/event.html')

def about(request):
    return render(request, 'pages/about.html')