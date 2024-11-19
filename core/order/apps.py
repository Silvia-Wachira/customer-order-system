from django.apps import AppConfig
# from core.order.viewsets import SendSMS


class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.order'
    label = 'core_order'

