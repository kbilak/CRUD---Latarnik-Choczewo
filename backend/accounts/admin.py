from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_joined', 'user_type']
    list_editable = ['user_type']
    search_fields = ['email', 'date_joined']
    list_filter = ['user_type']
