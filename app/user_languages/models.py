from django.db import models
from users.models import Users
from languages.models import Languages

class UserLanguages(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    lang_code = models.ForeignKey(Languages, on_delete=models.CASCADE)
    native_lang = models.BooleanField(default=False)
    active_lang = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserVocabulary(models.Model):
    id = models.AutoField(primary_key=True)
    lang_code = models.ForeignKey(UserLanguages, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    note = models.TextField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)