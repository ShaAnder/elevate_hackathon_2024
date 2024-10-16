from django.apps import AppConfig


class JobMeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "job_me"

    def ready(self):
        import job_me.signals
