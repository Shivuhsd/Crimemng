# Generated by Django 4.0 on 2021-12-23 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0007_remove_profile_accuser_remove_profile_accuseraddress_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
