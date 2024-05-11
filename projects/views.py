from django.shortcuts import render
from django.views import View

from projects.models import Project


class ProjectsListView(View):
    def get(self, request, *args, **kwargs):
        products = Project.objects.all()
        return render(request, 'projects/projects.html', {'products': products})
