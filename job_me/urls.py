from django.urls import path
from . import views

app_name = "job_me"

urlpatterns = [
    path("", views.home, name="home"),
]
