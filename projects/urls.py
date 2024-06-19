from django.urls import path

from projects.views import (
    ProjectsListView,
    ProjectDetailView,
    CartView,
    AccountView,
    ProjectCreateView,
    AddToCartView
)

app_name = 'projects'

urlpatterns = [
    path('search/', ProjectsListView.as_view(), name='search'),
    path('projects/', ProjectsListView.as_view(), name='projects'),
    path('cart/', CartView.as_view(), name='cart'),
    path('account/', AccountView.as_view(), name='account'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/project_create/', ProjectCreateView.as_view(), name='project_create'),
    path('add_to_cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
]

