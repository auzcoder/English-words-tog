from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUsers


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUsers
    list_display = ("get_full_name", 'user_id', "email", "mobile", "is_active_display", "is_staff", "is_superuser")
    def is_active_display(self, obj):
        if obj.is_active:
            return format_html('<i class="fa fa-solid fa-check-circle fa-solid" style="color: #19d225;"></i>')
        else:
            return format_html('<i class="fas fa-solid fa-times-circle" style="color: #f0380a;"></i>')

    is_active_display.short_description = "Holati"

    # list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        ("Foydalanuvchi sozlamalari", {"fields": ("username", "first_name", "last_name", "email", "mobile", "image", 'password' )}),
        ("Foydalanuvchi Huquqlari", {"fields": ("is_staff", 'is_active', 'is_superuser', "groups", "user_permissions")}),
        # ("Parolni yangilash", {"fields": ("password", '')}),
    )
    add_fieldsets = (
        ("Foydalanuvchi yaratish", {
            "classes": ("wide",),
            "fields": (
                "username", "first_name", "last_name", "email", "mobile", "image", "password1", "password2", "groups",
            )
        }
        ),
    )
    search_fields = ("email", "first_name", "last_name", "username")
    ordering = ("email", 'username')

admin.site.register(CustomUsers, CustomUserAdmin)


