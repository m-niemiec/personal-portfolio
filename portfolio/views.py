from django.shortcuts import render, get_object_or_404
from .models import Project


def home(request):
    projects = Project.objects.order_by('-created')
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/home.html', context)


def project_details(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {
        'project': project
    }
    return render(request, 'portfolio/project_details.html', context)
