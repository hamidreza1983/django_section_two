from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ( 'email' , 'is_staff', 'is_active')
    list_filter = ('is_active',)
    ordering = ['is_staff']
    fieldsets = (
        ('authentication', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),

    )
    add_fieldsets = (

        ("authentication", {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        )

admin.site.register(User, CustomUserAdmin)

# Register your models here.
