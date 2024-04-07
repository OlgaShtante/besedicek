from django.contrib import admin
from .models import User

class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    list_filter = ('created_at',)

admin.site.register(User, UsersAdmin)