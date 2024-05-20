from django.urls import path

from projects.views import (
    ProjectsListView,
    ProjectDetailView
)

app_name = 'projects'

urlpatterns = [
    path('projects/', ProjectsListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]

