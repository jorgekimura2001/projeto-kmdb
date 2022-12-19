from users.models import User
from django.core.management.base import BaseCommand, CommandError
import ipdb


class Command(BaseCommand):
    help = "Create admin users"

    def add_arguments(self, parser):
        # ipdb.set_trace()
        parser.add_argument(
            "--username",
            type=str,
        )
        parser.add_argument(
            "--password",
            type=str,
        )
        parser.add_argument(
            "--email",
            type=str,
        )

    def handle(self, *args, **kwargs):

        username = kwargs["username"]
        password = kwargs["password"]
        email = kwargs["email"]

        if not username:
            username = "admin"
        if not password:
            password = "admin1234"
        if not email:
            email = f"{username}@example.com"

        try:
            user_already_exists = User.objects.get(
                username=username,
                email=email,
            )
            ipdb.set_trace()
            if user_already_exists.username == username:
                raise CommandError(
                    f"Username {username} already taken.",
                )
            if user_already_exists.email == email:
                raise CommandError(
                    f"Email {email} already taken.",
                )
        except User.DoesNotExist:
            User.objects.create_superuser(
                username=username,
                password=password,
                email=email,
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Admin {username} successfully created!",
                )
            )
