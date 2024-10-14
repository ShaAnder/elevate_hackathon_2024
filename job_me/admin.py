from django.contrib import admin
from .models import (
    Category,
    Technology,
    Module,
    Topic,
    Question,
    UserQuestionKnowledge,
    UserTechnologyProgress,
)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "image")
    search_fields = ("name", "category__name")
    list_filter = ("category",)
    ordering = ("name",)


class ModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "technology")
    search_fields = ("title", "technology__name")
    list_filter = ("technology",)
    ordering = ("title",)


class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "module")
    search_fields = ("title", "module__title")
    list_filter = ("module",)
    ordering = ("title",)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "topic", "difficulty", "created_at", "updated_at")
    search_fields = ("title", "topic__title")
    list_filter = ("difficulty", "topic")
    ordering = ("created_at",)
    prepopulated_fields = {"title": ("title",)}


class UserQuestionKnowledgeAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "knowledge_status")
    search_fields = ("user__username", "question__title")
    list_filter = ("knowledge_status",)
    ordering = ("user",)


class UserTechnologyProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "technology", "progress_percentage")
    search_fields = ("user__username", "technology__name")
    list_filter = ("technology",)
    ordering = ("user",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserQuestionKnowledge, UserQuestionKnowledgeAdmin)
admin.site.register(UserTechnologyProgress, UserTechnologyProgressAdmin)
