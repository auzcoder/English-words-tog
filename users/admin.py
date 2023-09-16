from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUsers


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUsers
    list_display = ("first_name", 'user_id', "email", "mobile", "is_active_display",)
    def is_active_display(self, obj):
        if obj.is_active:
            return format_html('<i class="fa fa-solid fa-check-circle fa-solid" style="color: #19d225;"></i>')
        else:
            return format_html('<i class="fas fa-solid fa-times-circle" style="color: #f0380a;"></i>')

    is_active_display.short_description = "Holati"

    # list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("first_name", "last_name", "user_id", "email", "mobile", "image", "password", )}),
        ("Foydalanuvchi Huquqlari", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name", "last_name", "user_id", "email", "mobile", "image", "password1",
                "password2", "is_staff", "is_superuser", "groups", "user_permissions"
            )
        }
        ),
    )
    search_fields = ("email", "first_name", "last_name", "age")
    ordering = ("email",)


admin.site.register(CustomUsers, CustomUserAdmin)


