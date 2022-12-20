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

        username = kwargs.get("username")
        password = kwargs.get("password")
        email = kwargs.get("email")

        try:
            if not username:
                username = 'admin'
            else:
                # se passado segue abaixo
                username_already_exists = User.objects.get(
                    # se o username existir no db vai pro if
                    # se não retorna does not exist
                    username=username,
                )
                if username_already_exists.username == username:
                    raise CommandError(
                        f"Username `{username}` already taken.",
                    )

            if not email:
                email = f'{username}@example.com'
            else:
                email_already_exists = User.objects.get(
                    email=email,
                )
                if email_already_exists.email == email:
                    raise CommandError(
                        f"Email {email} already taken.",
                    )

            if not password:
                password = 'admin1234'

            raise User.DoesNotExist

        except User.DoesNotExist:
            if username == 'admin':
                raise CommandError(
                        f"Username `{username}` already taken.",
                    )
            if email == 'admin@example.com':
                raise CommandError(
                        f"Email {email} already taken.",
                    )
            User.objects.create_superuser(
                username=username or 'admin',
                password=password or 'admin1234',
                email=email or f'{username}@example.com',
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Admin `{username}` successfully created!",
                )
            )
