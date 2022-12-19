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

        username = kwargs.get("username") or 'admin'
        password = kwargs.get("password") or 'admin1234'
        email = kwargs.get("email") or f'{username}@example.com'

        try:
            username_already_exists = User.objects.get(
                username=username,
            )
            email_already_exists = User.objects.get(
                email=email,
            )
            if username_already_exists.username == username:
                raise CommandError(
                    f"Username {username} already taken.",
                )
            if email_already_exists.email == email:
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
