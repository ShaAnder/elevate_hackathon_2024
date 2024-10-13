from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("", include("job_me.urls")),
    path("accounts/", include("allauth.urls")),
]
