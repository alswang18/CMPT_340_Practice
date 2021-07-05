from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    duration = models.FloatField(blank=True)
    cover = models.ImageField(upload_to="", blank=True)