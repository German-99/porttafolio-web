from django.urls import path
from .views import certifications

app_name = "certifications"

urlpatterns = [

path('' ,certifications, name='certificates'),
]