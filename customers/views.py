from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from customers.forms import RegistrationModelForm
from customers.models import Customer


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customers/login.html', {})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('projects:projects'))
        return render(request, 'customers/login.html', {})


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationModelForm()
        return render(request, 'customers/registration.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationModelForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.phone = form.cleaned_data['phone']
            new_user.address = form.cleaned_data['address']
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Customer.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
            )
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect(reverse('projects:projects'))
        return render(request, 'customers/registration.html', {'form': form})
