from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            'first_name',
            'last_name',
            'bio',
            'is_critic',
            'is_superuser',
            'updated_at',
            'password',
            'username'
        ]
        read_only_field = ['is_superuser']
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message='user with this email already exists.',
                    )
                ]
            },
        }
