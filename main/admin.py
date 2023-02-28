from django.contrib import admin
from .models import   Theater,Screen,Seat,Movies

# Register your models here.
admin.site.register(Theater)
admin.site.register(Screen)
admin.site.register(Seat)

admin.site.register(Movies)
