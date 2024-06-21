from django.contrib.auth.models import User
from django.db import models


class NotificationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def alle(self, recipient):
        return super().get_queryset().filter(
            recipient=recipient,
            read=False
        )

    def make_all_read(self, recipient):
        qs = self.get_queryset().filter(
            recipient=recipient,
            read=False
        )
        qs.update(read=True)


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
    objects = NotificationManager()
