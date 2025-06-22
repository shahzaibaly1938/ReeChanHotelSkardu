from django.db import models
from datetime import datetime
from Accommodation.models import Feature

# Create your models here.
class Table_Reservation(models.Model):
    guest_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    start_time = models.TimeField(default=datetime.now())
    end_time = models.TimeField()
    reserve_date = models.DateField()
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.guest_name} - start: {self.start_time} - end: {self.end_time} - contact:{self.phone_number} "


class MeetingsnEvent(models.Model):
    guest_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    start_time = models.TimeField(default=datetime.now())
    end_time = models.TimeField()
    reserve_date = models.DateField()
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.guest_name} - start: {self.start_time} - end: {self.end_time} - contact:{self.phone_number} "
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='restaurant/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Special_Dish(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Dishe(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='dishes/', blank=True, null=True)
    image2 = models.ImageField(upload_to='dishes/', blank=True, null=True)
    image3 = models.ImageField(upload_to='dishes/', blank=True, null=True)
    image4 = models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name



class Aboutus(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='hotel_image/', blank=True, null=True)
    image2 = models.ImageField(upload_to='hotel_image/', blank=True, null=True)
    image3 = models.ImageField(upload_to='hotel_image/', blank=True, null=True)

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

    def __str__(self):
        return self.name
    

class Contactus(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Home(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='hotel_image/', blank=True, null=True)
    whychose = models.ManyToManyField(Feature, default='')


    def __str__(self):
        return self.name