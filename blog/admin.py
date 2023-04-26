from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('title', 'author')



admin.site.register(Post,PostAdmin)
admin.site.register(Category)
# Register your models here.
