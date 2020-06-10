from django.apps import AppConfig


class UserpostConfig(AppConfig):
    name = 'userpost'

    def ready(self):
        import userpost.signals
