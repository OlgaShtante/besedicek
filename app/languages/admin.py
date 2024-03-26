from django.contrib import admin
from .models import Languages

class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_filter = ('code',)

admin.site.register(Languages, LanguagesAdmin)

