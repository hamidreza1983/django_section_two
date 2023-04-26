from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ( 'email' , 'is_staff', 'is_active')
    list_filter = ('is_active',)
    ordering = ['is_staff']
    fieldsets = (
        ('authentication', 
            {'fields': ('email', 'password')}
        ),
        ('Permissions', 
            {'fields': ('is_staff', 'is_active', 'is_superuser')}
        ),
        ('group permissions', 
            {'fields': ('groups', 'user_permissions',)}
        ),
        ('important date', 
            {'fields': ('last_login',)}
        ),

    )

    add_fieldsets = (

        ("authentication", 
            {"fields": ("email", "password1","password2")}
        ),
        ("Permissions", 
            {"fields": ("is_staff", "is_active", "is_superuser")}
        ),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)

# Register your models here.
