from django.shortcuts import render
from  .models import Certification

# Create your views here.

def home(request): 
    certifications = Certification.objects.all()

    return render(request, 'home.html', {'certifications': certifications})