from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    movie_id = serializers.SerializerMethodField()

    critic = serializers.SerializerMethodField()

    def get_critic(self, obj: Review) -> dict:
        return {
            "id": obj.critic.pk,
            "first_name": obj.critic.first_name,
            "last_name": obj.critic.last_name,
        }

    def get_movie_id(self, obj: Review) -> str:
        return obj.movie.pk

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "movie_id",
            "critic",
            'spoilers'
        ]
