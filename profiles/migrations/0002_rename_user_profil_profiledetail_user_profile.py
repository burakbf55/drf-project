# Generated by Django 3.2.9 on 2021-12-08 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiledetail',
            old_name='user_profil',
            new_name='user_profile',
        ),
    ]