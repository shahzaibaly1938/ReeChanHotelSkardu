from django.db import models
from datetime import datetime

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