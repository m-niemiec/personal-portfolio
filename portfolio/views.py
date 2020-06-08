from django.shortcuts import render, get_object_or_404
from .models import Project


def home(request):
    projects = Project.objects.order_by('-created')
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/home.html', context)


# Project details when you click "Details" from main Projects listing.
def project_details(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    next_project = Project.objects.filter(id__gt=project_id).order_by('id').first()
    previous_project = Project.objects.filter(id__lt=project_id).order_by('-id').first()
    context = {
        'project': project,
        'next_project': next_project,
        'previous_project': previous_project
    }
    return render(request, 'portfolio/project_details.html', context)
