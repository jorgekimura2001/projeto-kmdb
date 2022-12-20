from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    stars = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )
    review = models.TextField()
    spoilers = models.BooleanField(default=False)

    movie = models.ForeignKey(
        'movies.Movie',
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    critic = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
