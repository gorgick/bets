from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from customers.models import Customer
from projects.forms import ProjectCreateForm
from projects.mixins import CartMixin
from projects.models import Project, Cart
from projects.utils import q_search


class ProjectsListView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        query = request.GET.get('q', None)
        if query:
            products = q_search(query)
        else:
            products = Project.objects.all()
        paginator = Paginator(products, 3)
        current_page = paginator.page(int(page))
        return render(request, 'projects/projects.html', {'products': current_page, 'cart': self.cart})


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


class AddToCartView(CartMixin, View):
    def post(self, request, *args, **kwargs):
        qty = request.POST.get('qty')
        project = Project.objects.get(id=kwargs.get('pk'))
        new_bettor = Customer.objects.get(user=request.user)
        if float(qty) > project.price:
            project.price = qty
            if project.bettor != new_bettor and project.bettor is not None:
                cart = Cart.objects.get(owner=project.bettor)
                cart.products.remove(project)
                self.cart.save()
            project.bettor = new_bettor
            project.save()
            self.cart.products.add(project)
            self.cart.save()
        else:
            pass
        return render(request, 'projects/cart.html', {'cart': self.cart})
