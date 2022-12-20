from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminOrCriticOrReadOnly
from .models import Review
from .serializers import ReviewSerializer
import ipdb
from movies.models import Movie
from django.shortcuts import get_object_or_404


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCriticOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        movie_obj = get_object_or_404(Movie, pk=movie_id)

        reviews = Review.objects.filter(movie=movie_obj)

        return reviews

    def perform_create(self, serializer):
        movie_id = self.kwargs['movie_id']
        movie_obj = get_object_or_404(Movie, pk=movie_id)
        # ipdb.set_trace()
        serializer.save(critic=self.request.user, movie_id=movie_obj.id)
