from django.apps import AppConfig


class ResturantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Resturant'
def ready(self):
    import Resturant.signals  # غيّر الاسم حسب تطبيقك
