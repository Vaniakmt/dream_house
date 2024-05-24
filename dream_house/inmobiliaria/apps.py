from django.apps import AppConfig


class InmobiliariaConfig(AppConfig):
    name = 'inmobiliaria'

    def ready(self):
        import inmobiliaria.signals