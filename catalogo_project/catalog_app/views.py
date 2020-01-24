from django.shortcuts import render
from .models import Actor, Movie
from .serializers import ActorSerializer, MovieSerializer
from rest_framework import viewsets

# Create your views here.
class ActorAPI(viewsets.ModelViewSet):
    queryset = Actor.objects.all().order_by('id')
    serializer_class = ActorSerializer

class MovieAPI(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer
