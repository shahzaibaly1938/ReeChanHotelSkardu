from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=400)
    svg = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = "Content Features"
        verbose_name_plural = "Content Features"

    def __str__(self):
        return self.name
    
class Room_type(models.Model):
    name = models.CharField(max_length=50)
    no_of_rooms = models.IntegerField()
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    cover_image = models.ImageField(upload_to="room_images/", blank=True, null=True)
    image_2 = models.ImageField(upload_to="room_images/", blank=True, null=True)
    image_3 = models.ImageField(upload_to="room_images/", blank=True, null=True)
    image_4 = models.ImageField(upload_to="room_images/", blank=True, null=True)
    image_5 = models.ImageField(upload_to="room_images/", blank=True, null=True)
    description = models.TextField(max_length=500, default='')
    features = models.ManyToManyField(Feature, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Content Room_Type"
        verbose_name_plural = "Content Room_Types"


    def __str__(self):
        return self.name
    


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    check_in = models.DateField()
    check_out = models.DateField()
    room_type = models.CharField(max_length=50)
    no_of_rooms = models.IntegerField()
    adults = models.IntegerField()
    children = models.IntegerField()

    class Meta:
        verbose_name = "Data Bookings"
        verbose_name_plural = "Data Bookings"


    def __str__(self):
        return f"{self.name} - {self.phone_number} _ CheckIn {self.check_in} _ CheckOut {self.check_out}"



