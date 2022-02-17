from turtle import title
from django.db import models

# Create your models here.

class Carousel(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField()

    image = models.ImageField(upload_to = 'carousel/')
    creation_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
