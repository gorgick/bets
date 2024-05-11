from django.urls import path

from projects.views import ProjectsListView

app_name = 'projects'

urlpatterns = [
    path('projects/', ProjectsListView.as_view(), name='projects'),
]

