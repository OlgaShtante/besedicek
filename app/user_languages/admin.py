from django.contrib import admin
from .models import UserLanguages, UserVocabulary

class UserLanguagesAdmin(admin.ModelAdmin):
    list_display = ('lang_code', 'active_lang', 'native_lang')
    list_filter = ('active_lang',)

class UserVocabularyAdmin(admin.ModelAdmin):
    list_display = ('word', 'note', 'created_at','updated_at')
    list_filter = ('updated_at',)


admin.site.register(UserLanguages, UserLanguagesAdmin)
admin.site.register(UserVocabulary, UserVocabularyAdmin)


