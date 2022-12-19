from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser

from .models import User
from .serializers import UserSerializer

from .permissions import IsAdminOrCreateOnly

import ipdb

from rest_framework import generics


# class UserView(APIView, PageNumberPagination):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [
#         # IsAuthenticated,
#         IsAdminOrReadOnly,
#     ]

#     def get(self, request: Request) -> Response:

#         """
#         Listagem de usuários
#         """
#         users = User.objects.all()
#         result_page = self.paginate_queryset(users, request)
#         serializer = UserSerializer(result_page, many=True)
#         ipdb.set_trace()
#         self.check_object_permissions(request, users)
#         return self.get_paginated_response(serializer.data)

#     def post(self, request: Request) -> Response:
#         """
#         Registro de usuários
#         """
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         return Response(serializer.data, status.HTTP_201_CREATED)


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCreateOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        self.check_object_permissions(self.request, self.request.user)
        return self.queryset
