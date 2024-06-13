from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from customers.models import Customer
from projects.forms import ProjectCreateForm
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


class ProjectCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ProjectCreateForm(request.POST, request.FILES)
        return render(request, 'projects/project_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProjectCreateForm(request.POST, request.FILES)
        customer = Customer.objects.get(user=request.user)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.creator = customer
            new_project.save()
            return redirect(reverse('projects:projects'))
        return render(request, 'projects/project_create.html', {'form': form})
