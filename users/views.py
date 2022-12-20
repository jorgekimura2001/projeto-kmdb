from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser

from .models import User
from .serializers import UserSerializer

from .permissions import IsAdminOrCreateOnly

from rest_framework import generics


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCreateOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer
