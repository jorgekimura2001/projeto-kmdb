from rest_framework import generics
from .serializers import MovieSerializer
from .models import Movie
from users.permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import ipdb


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        self.check_object_permissions(self.request, self.request.user)
        ipdb.set_trace()
        serializer.save(user=self.request.user)
