from django.db import models
from django.urls import reverse

from customers.models import Customer


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    image = models.ImageField(upload_to='projects/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='projects')
    bettor = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bet_projects', null=True, blank=True)
    archived = models.BooleanField(default=False)
    cart_flag = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('projects:project_detail', kwargs={'pk': self.id})



class Cart(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')
    products = models.ManyToManyField(Project, blank=True, related_name='carts')
    final_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    in_order = models.BooleanField(default=False)
