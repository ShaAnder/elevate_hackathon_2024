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
    path("questions/<int:question_id>/", views.question_detail, name="question_detail"),
    path(
        "modules/<int:module_id>/first-question/",
        views.redirect_to_first_question_from_module,
        name="redirect_to_first_question_module",
    ),
    path(
        "topics/<int:topic_id>/first-question/",
        views.redirect_to_first_question_from_topic,
        name="redirect_to_first_question_topic",
    ),
    path(
        "update_knowledge_status/<int:question_id>/",
        views.update_knowledge_status,
        name="update_knowledge_status",
    ),
    path(
        "technology/<int:technology_id>/calculate_progress/",
        views.calculate_user_progress,
        name="calculate_user_progress",
    ),
]
