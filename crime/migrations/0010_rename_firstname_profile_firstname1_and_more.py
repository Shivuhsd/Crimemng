# Generated by Django 4.0 on 2021-12-23 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0009_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='firstname',
            new_name='firstname1',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='lastname',
            new_name='lastname1',
        ),
    ]