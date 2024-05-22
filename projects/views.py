from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from customers.models import Customer
from projects.mixins import CartMixin
from projects.models import Project


class ProjectsListView(View):
    def get(self, request, *args, **kwargs):
        products = Project.objects.all()
        return render(request, 'projects/projects.html', {'products': products})


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'product'


class CartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'projects/cart.html', {'cart': self.cart})


class AccountView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        return render(request, 'projects/account.html', {'cart': self.cart, 'customer': customer})
