from django.contrib import admin
from .models import Room_type, Booking, Feature
# Register your models here.
admin.site.register(Room_type)
admin.site.register(Booking)
admin.site.register(Feature)

admin.site.site_header = "ReeChan Resort Skardu - Admin Panel"
admin.site.site_title = "ReeChan Resort Skardu Portal"
admin.site.index_title = "Welcome to ReeChan Resort Skardu Dashboard"