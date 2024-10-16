from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("", include("job_me.urls")),
    path("accounts/", include("allauth.urls")),
]

handler404 = 'job_me.views.custom_404'
handler500 = 'job_me.views.custom_500'
