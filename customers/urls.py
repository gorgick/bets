from django.contrib.auth.views import LogoutView
from django.urls import path

from customers.views import LoginView, RegistrationView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page=('projects:projects')), name='logout'),
]