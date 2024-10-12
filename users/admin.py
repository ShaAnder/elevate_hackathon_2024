from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, CustomUser


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name")


admin.site.register(Profile, UserProfileAdmin)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(CustomUser, CustomUserAdmin)
