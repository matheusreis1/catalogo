from rest_framework import serializers
from .models import Actor, Movie
from rest_framework.utils import model_meta

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'age')

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        actors_data = validated_data.pop('actors')
        movie = Movie.objects.create(**validated_data)

        for actor in actors_data:
            actor, created = Actor.objects.get_or_create(
                name=actor['name'], age=actor['age']
            )
            movie.actors.add(actor)

        return movie

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        actors_data = validated_data.pop('actors')
        
        for actor in actors_data:
            try:
                actor_db = Actor.objects.get(
                    movie=instance, name=actor['name']
                )
                actor_db.name = actor['name']
                actor_db.age = actor['age']
                actor_db.save()
            except Actor.DoesNotExist:
                actor_db = Actor.objects.create(
                    movie=instance, **actor
                )
                instance.actors.add(actor_db)

        actors_db = Actor.objects.filter(
            movie=instance
        )
        for actor_db in actors_db:
            is_missing = True
            for actor in actors_data:
                if actor['name'] == actor_db.name:
                    is_missing = False
            if is_missing:
                Actor.objects.get(
                    id=actor_db.id
                ).delete()

        return instance
