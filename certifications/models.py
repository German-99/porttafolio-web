from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Certification(models.Model):
    title = CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = ImageField(upload_to= 'images/certifications')
    lenguages = models.ForeignKey("ProgramLenguage", on_delete=models.CASCADE)
    url = URLField(blank=True)

    def __str__(self):
        return self.title 

   


class ProgramLenguage(models.Model):
    choice = models.CharField(max_length=20)
    icon = ImageField(upload_to= 'images/icons', null=True, blank=True)
   
    def __str__(self):
        return self.choice 

