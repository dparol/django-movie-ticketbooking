from rest_framework import serializers
from .models import *


class Theaterserializer(serializers.ModelSerializer):
    class  Meta:
       model=Theater
       fields='__all__'
       
class Screenserializer(serializers.ModelSerializer):
    class  Meta:
        model = Screen
        fields='__all__'

class Seatserializer(serializers.ModelSerializer):
    class Meta:
        model= Seat
        fields='__all__'

class movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields ="__all__"