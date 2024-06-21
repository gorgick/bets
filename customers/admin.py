from django.contrib import admin

from .models import Customer, Notification

admin.site.register(Customer)
admin.site.register(Notification)
