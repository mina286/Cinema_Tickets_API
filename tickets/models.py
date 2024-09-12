from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    hall = models.CharField(max_length=100)
    movie = models.CharField(max_length=100)
    date = models.DateField(null=True)
    def __str__(self) :
        return  f"{self.movie} {self.hall}"
    
    class Meta:
        db_table = 'Movie'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class Guest(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)

    def __str__(self) :
        return  f"{self.name}"
    
    class Meta:
        db_table = 'Guest'
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'

class Reservation(models.Model):
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE,related_name='guest_reservation')
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='novie_reservation')

    def __str__(self) :
        return  f"{self.guest} {self.movie}"
    
    class Meta:
        db_table = 'Reservation'
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'