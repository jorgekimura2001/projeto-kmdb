from rest_framework import serializers
from .models import Movie
from genres.serializers import GenreSerializer
import ipdb
from genres.models import Genre


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    def create(self, validated_data: dict) -> Movie:

        request_genres = validated_data.pop('genres')
        # ipdb.set_trace()
        movie = Movie.objects.create(**validated_data)
        for genre in request_genres:
            genre_request, _ = Genre.objects.get_or_create(**genre)
            movie.genres.add(genre_request)
        return movie

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            'genres'
        ]
        # read_only_fields = ['user']
