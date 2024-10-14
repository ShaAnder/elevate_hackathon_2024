from django.urls import path
from . import views

app_name = "job_me"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("categories/", views.category_list, name="categories"),
    path(
        "technologies/<int:technology_id>/",
        views.technology_detail,
        name="technology_detail",
    ),
]
