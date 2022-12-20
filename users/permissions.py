from rest_framework import permissions
from .models import User
from rest_framework.views import Request
import ipdb


class IsAdminOrCreateOnly(permissions.BasePermission):
    def has_permission(
        self,
        request: Request,
        view,
    ) -> bool:
        if request.method not in permissions.SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.user.is_superuser:
            return True
        else:
            return False


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(
        self,
        request: Request,
        view,
    ) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.user.is_superuser:
            return True
        else:
            return False


class IsAdminOrCriticOrReadOnly(permissions.BasePermission):
    def has_permission(
        self,
        request: Request,
        view,
    ) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.user.is_superuser or request.user.is_authenticated and request.user.is_critic:
            return True
        else:
            return False
