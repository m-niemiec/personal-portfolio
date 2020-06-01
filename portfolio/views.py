from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.order_by('-created')
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/home.html', context)
