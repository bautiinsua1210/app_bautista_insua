from django.contrib import admin
from .models import Car, Client, Service


admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Service)