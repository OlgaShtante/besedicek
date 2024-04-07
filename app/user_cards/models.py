from django.db import models
from user_languages.models import UserVocabulary
from user.models import User

STATUS_CHOICES = [
    ('NEW', 'New'),
    ('IN_PROGRESS', 'In Progress'),
    ('DONE', 'Done'),
]

class UserCard(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    card_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_cards'

class UserWordCard(models.Model):
    id = models.AutoField(primary_key=True)
    user_vocabulary_id = models.ForeignKey(UserVocabulary, on_delete=models.CASCADE)
    card_id = models.ForeignKey(UserCard, on_delete=models.CASCADE)
    word_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_words_in_card'