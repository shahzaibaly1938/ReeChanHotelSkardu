from django.contrib import admin
from .models import Table_Reservation, MeetingsnEvent, Contact, Restaurant, Special_Dish, Dishe, Aboutus, MeetingsPage,Contactus,Home
from Accommodation.models import Room_type
# Register your models here.

admin.site.register(MeetingsnEvent)
admin.site.register(Contact)
admin.site.register(Table_Reservation)
admin.site.register(Restaurant)
admin.site.register(Special_Dish)
admin.site.register(Dishe)
admin.site.register(Aboutus)
admin.site.register(MeetingsPage)
admin.site.register(Contactus)
admin.site.register(Home)
admin.site.register(Room_type)
