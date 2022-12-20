from users.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create admin users"

    def add_arguments(self, parser):

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

        username = kwargs.get("username") or "admin"
        password = kwargs.get("password") or "admin1234"
        email = kwargs.get("email") or f"{username}@example.com"

        username_already_exists = User.objects.filter(username=username).exists()

        if username_already_exists:
            raise CommandError(
                f"Username `{username}` already taken.",
            )

        email_already_exists = User.objects.filter(email=email).exists()

        if email_already_exists:
            raise CommandError(
                f"Email `{email}` already taken.",
            )

        User.objects.create_superuser(
                username=username,
                password=password,
                email=email,
            )
        self.stdout.write(
            self.style.SUCCESS(
                f"Admin `{username}` successfully created!",
            )
        )
