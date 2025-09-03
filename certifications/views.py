from django.shortcuts import render
from  .models import Certification

# Create your views here.

def certifications(request): 
    certifications = Certification.objects.all().order_by('date')

    return render(request, 'home.html', {'certifications': certifications})