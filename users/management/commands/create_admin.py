from users.models import User
from django.core.management.base import BaseCommand, CommandError
import ipdb

# primeiro verificar se o usuário passou os campos opcionais


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

        # try:
        #     if not username and not email:
        #         # ipdb.set_trace()
        #         # se o usuario nao passar email e username
        #         username = 'admin'
        #     elif username:
        #         # caso o usuário tenha passado segue abaixo
        #         # verifica se o username já tem no banco
        #         # caso tenha entra no if e estoura um CommandError
        #         # caso não tenha, entra no doesnotexist
        #         username_already_exists = User.objects.get(
        #             username=username,
        #         )
        #         if username_already_exists.username == username:
        #             raise CommandError(
        #                 f"Username `{username}` already taken.",
        #             )
        #     # caso o usuario passe o email e não o username
        #     if not email:
        #         email = f'{username}@example.com'
        #     else:
        #         username = email.split('@')[0]
        #         # caso o usuario não tenha passado username
        #         email_already_exists = User.objects.get(
        #             email=email,
        #         )
        #         if email_already_exists.email == email:
        #             raise CommandError(
        #                 f"Email {email} already taken.",
        #             )

        #     if not password:
        #         password = 'admin1234'
        #     # ipdb.set_trace()
        #     # verificar se já existe um admin
        #     # caso exista já irá entrar no if gerar o CommandError
        #     # caso não exista dispara um User.DoesNotExists

        #     username_already_exists = User.objects.get(
        #             username='admin',
        #     )
        #     if username_already_exists:
        #         raise CommandError(
        #             f"Username `{username}` already taken.",
        #         )

        #     email_already_exists = User.objects.get(
        #             email='admin@example.com',
        #         )
        #     if email_already_exists:
        #         raise CommandError(
        #             f"Email `{email}` already taken.",
        #         )

        #     User.objects.create_superuser(
        #         username=username,
        #         password=password or 'admin1234',
        #         email=email or f'{username}@example.com',
        #     )
        #     self.stdout.write(
        #         self.style.SUCCESS(
        #             f"Admin `{username}` successfully created!",
        #         )
        #     )

        # except User.DoesNotExist:

        #     # email_already_exists = User.objects.get(
        #     #         email='admin@example.com',
        #     #     )
        #     # if email_already_exists:
        #     #     raise CommandError(
        #     #         f"Email `{email}` already taken.",
        #     #     )

        #     # ipdb.set_trace()
        #     User.objects.create_superuser(
        #         username=username,
        #         password=password or 'admin1234',
        #         email=email or f'{username}@example.com',
        #     )
        #     self.stdout.write(
        #         self.style.SUCCESS(
        #             f"Admin `{username}` successfully created!",
        #         )
        #     )
