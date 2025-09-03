from django.db import models
from django.db.models.fields import CharField, URLField, DateField
from django.db.models.fields.files import ImageField
from certifications.models import ProgramLenguage
# Create your models here.

class Project(models.Model):
    title = CharField(max_length=100)
    description = models.CharField(max_length=250)
    largeDescription = models.TextField(null=True, blank=True)
    image = ImageField(upload_to= 'images/projects')
    lenguages = models.ManyToManyField("certifications.ProgramLenguage")
    gif = ImageField(upload_to= 'images/gifs')
    date = DateField(null=True, blank=True)
    url = URLField(blank=True)

    def __str__(self):
        return self.title 