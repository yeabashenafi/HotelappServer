from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Room,Booking,Event

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['number','url','Type','isBooked','price']

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['number','url','room','bookedBy','bookedDate',
        'bookedUntil']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','password','first_name',
        'last_name']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['url','id','name','detail','startDate','startTime','endDate','endTime',
        'availableSpaces',
        'price']