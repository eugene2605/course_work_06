from django.apps import AppConfig


class MailingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailings'
    verbose_name = 'рассылки'

    # def ready(self):
    #     from mailings.management.commands import start_mailings
    #     start_mailings.Command.handle(self)
