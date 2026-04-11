from django.apps import AppConfig


class AuthxConfig(AppConfig):
    name = '{{cookiecutter.project_slug}}.apps.authx'
    verbose_name = "Auth"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
