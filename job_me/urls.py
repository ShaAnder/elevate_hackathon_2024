from django.urls import path
from . import views
# from .views import trigger_500_error

app_name = "job_me"

urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.categories, name="categories"),
    path("about/", views.about, name="about"),
    # path('trigger-500/', trigger_500_error),

]
