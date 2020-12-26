from django.shortcuts import render
from .models import Project


def index(request):
    context = {
        "projects": Project.objects.all()
    }
    return render(request, 'projects/index.html', context)


def detail(request, id):
    context = {
        "project": Project.objects.get(pk=id)
    }
    return render(request, 'projects/detail.html', context)
