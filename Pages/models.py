from django.db import models
from datetime import datetime
from Accommodation.models import Feature
from django.utils import timezone

# Create your models here.
class Table_Reservation(models.Model):
    guest_name = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=12, default='')
    email = models.EmailField(default='')
    datetime = models.DateTimeField(default=timezone.now)
    reserved_for_hours = models.PositiveIntegerField(default=1)
    additional_info = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = "Data Table Reservation"
        verbose_name_plural = "Data Table Reservations"

    def __str__(self):
        return f"{self.guest_name} - date time: {self.datetime} - reserved for: {self.reserved_for_hours} hours - contact:{self.phone_number} "


class MeetingsnEvent(models.Model):
    guest_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(default='')
    address = models.TextField(default='')
    datetime = models.DateTimeField(default=timezone.now)
    reserved_for_hours = models.PositiveIntegerField(default=1)
    reserve_date = models.DateField(auto_now_add=True)
    additional_info = models.TextField(blank=True)

    class Meta:
        verbose_name = "Data Meeting & Event"
        verbose_name_plural = "Data Meeting & Events"

    def __str__(self):
        return f"{self.guest_name} - start: {self.datetime} - booked for : {self.reserved_for_hours} hours - contact:{self.phone_number} "
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = "Data Contact"
        verbose_name_plural = "Data Contacts"

    def __str__(self):
        return self.name
    


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='restaurant/', blank=True, null=True)

    class Meta:
        verbose_name = "Page Restaurant"
        verbose_name_plural = "Page Restaurants"


    def __str__(self):
        return self.name
    

class Special_Dish(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='dishes/', blank=True, null=True)

    class Meta:
        verbose_name = "Content Special Dish"
        verbose_name_plural = "Content Special Dishes"

    def __str__(self):
        return self.name
    
class Dishe(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='dishes/', blank=True, null=True)
    image2 = models.ImageField(upload_to='dishes/', blank=True, null=True)
    image3 = models.ImageField(upload_to='dishes/', blank=True, null=True)
    image4 = models.ImageField(upload_to='dishes/', blank=True, null=True)

    class Meta:
        verbose_name = "Item Dish"
        verbose_name_plural = "Item Dishes"

    def __str__(self):
        return self.name



class Aboutus(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='hotel_image/', blank=True, null=True)
    image2 = models.ImageField(upload_to='hotel_image/', blank=True, null=True)
    image3 = models.ImageField(upload_to='hotel_image/', blank=True, null=True)

    class Meta:
        verbose_name = "Page About us"
        verbose_name_plural = "Page About us"

    def __str__(self):
        return self.name
    
class MeetingsPage(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    heading2 = models.CharField(max_length=200, default='')
    image1 = models.ImageField(upload_to='hotel_image/', blank=True, null=True)
    image2 = models.ImageField(upload_to='hotel_image/', blank=True, null=True)
    image3 = models.ImageField(upload_to='hotel_image/', blank=True, null=True)
    image4 = models.ImageField(upload_to='hotel_image/', blank=True, null=True)

    class Meta:
        verbose_name = "Page Meetings & Event"
        verbose_name_plural = "Page Meetings & Events"

    def __str__(self):
        return self.name
    

class Contactus(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Page Contact"
        verbose_name_plural = "Page Contact"

    def __str__(self):
        return self.name


class Home(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='hotel_image/', blank=True, null=True)
    whychose = models.ManyToManyField(Feature, default='')

    class Meta:
        verbose_name = "Page Home"
        verbose_name_plural = "Page Home"


    def __str__(self):
        return self.name