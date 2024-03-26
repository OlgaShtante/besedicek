from django.contrib import admin
from .models import UserCard

class AdminCard(admin.ModelAdmin):
    list_display = ('title', 'card_status')
    list_filter = ('card_status',)


admin.site.register(UserCard, AdminCard)


