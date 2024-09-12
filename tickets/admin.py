from django.contrib import admin
from .models import Guest,Movie,Reservation

# 1
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','hall','movie','date']
    list_display_links = ['id','hall','movie','date']

admin.site.register(Movie,MovieAdmin)
# 2
class GuestAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile']
    list_display_links = ['id','name','mobile']
admin.site.register(Guest,GuestAdmin)
# 3
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id','guest','movie']
    list_display_links = ['id','guest','movie']
admin.site.register(Reservation,ReservationAdmin)