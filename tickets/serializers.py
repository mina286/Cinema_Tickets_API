from .models import Movie,Reservation,Guest
from rest_framework import serializers
from .models import Guest,Movie,Reservation

#  MovieSerializer
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields ="__all__"


# ReservationSerializer
class ReservationSerializer(serializers.ModelSerializer):
    # اول حل وهو تغير اسم العمود 
    # تانى حل وهو اخفاء العمود 
    # 1.1
    guest = serializers.SerializerMethodField(read_only =True)
    def get_guest(self,obj):
        return obj.guest.name
        
    #1.2
    movie = serializers.SerializerMethodField(read_only =True)
    def get_movie(self,obj):
        return obj.movie.movie
    
    class Meta:
        model = Reservation
        fields ="__all__"

# GuestSerializer
class GuestSerializer(serializers.ModelSerializer):
    
    reservation = serializers.SerializerMethodField(read_only=True)
    def get_reservation(self,obj):
            reservation = obj.guest_reservation.all()
            serializer = ReservationSerializer(reservation,many =True)
            return serializer.data
    
    class Meta:
        model = Guest
        fields ="__all__"
