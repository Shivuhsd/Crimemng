# Generated by Django 4.0.1 on 2022-01-21 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0025_profile_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='created_by',
            new_name='user',
        ),
    ]
