# Generated by Django 3.2.22 on 2024-04-07 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLanguages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('native_lang', models.BooleanField(default=False)),
                ('active_lang', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lang_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.languages')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user_languages',
            },
        ),
        migrations.CreateModel(
            name='UserVocabulary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=100)),
                ('note', models.TextField(max_length=350)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lang_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_languages.userlanguages')),
            ],
            options={
                'db_table': 'user_vocabulary',
            },
        ),
    ]
