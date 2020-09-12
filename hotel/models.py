from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    number = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=30)
    isBooked = models.BooleanField(default = False)
    price = models.FloatField()

class Booking(models.Model):
    number = models.AutoField(primary_key = True)
    room = models.ForeignKey(Room,on_delete = models.CASCADE)
    bookedBy = models.ForeignKey(User,on_delete = models.CASCADE)
    bookedDate = models.DateTimeField(auto_now = True)
    bookedUntil = models.DateField()

class Event(models.Model):
    name = models.CharField(max_length=200)
    detail = models.TextField(max_length=400)
    startDate = models.DateField()
    startTime = models.TimeField()
    endDate = models.DateField(null = True)
    endTime = models.TimeField(null = True)
    availableSpaces = models.IntegerField()
    price = models.FloatField()

