from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Notification(models.Model):
    recipient = models.ForeignKey(Customer, on_delete=models.CASCADE)
    text = models.TextField()
    read = models.BooleanField(default=False)