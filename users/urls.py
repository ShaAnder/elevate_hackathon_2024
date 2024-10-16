from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("profile/update/", views.update_profile, name="profile_update"),
    path("accounts/logout/", views.custom_logout, name="logout"),
]
