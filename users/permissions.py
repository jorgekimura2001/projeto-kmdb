from rest_framework import permissions
from .models import User
from rest_framework.views import Request
import ipdb


class IsAdminOrCreateOnly(permissions.BasePermission):
    def has_object_permission(
        self,
        request: Request,
        view,
        user: User,
    ) -> bool:
        # ipdb.set_trace()
        if request.method not in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(
        self,
        request: Request,
        view,
        # user: User,
    ) -> bool:
        # ipdb.set_trace()
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.user.is_superuser:
            return True
        else:
            return False
