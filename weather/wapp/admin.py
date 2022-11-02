from django.contrib import admin

# Register your models here.

from .models import Weather, City, Subscribed

admin.site.register(Weather)
admin.site.register(City)
admin.site.register(Subscribed)
