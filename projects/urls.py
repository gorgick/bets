from django.urls import path

from projects.views import (
    ProjectsListView,
    ProjectDetailView,
    CartView
)

app_name = 'projects'

urlpatterns = [
    path('projects/', ProjectsListView.as_view(), name='projects'),
    path('cart/', CartView.as_view(), name='cart'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]

