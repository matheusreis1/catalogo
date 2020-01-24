from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.FloatField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name