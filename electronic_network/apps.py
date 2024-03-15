from django.apps import AppConfig


class ElectronicNetworkConfig(AppConfig):
    """ Конфигурационные данные приложения. """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'electronic_network'
    verbose_name = 'Сеть электроники'
