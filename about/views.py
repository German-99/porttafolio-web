from django.shortcuts import render
from certifications.models import ProgramLenguage


def about(request):
    return render(request, 'about.html', {
        "lenguages": ProgramLenguage.objects.all()
    })
