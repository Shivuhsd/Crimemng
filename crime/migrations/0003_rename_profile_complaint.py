# Generated by Django 4.0 on 2021-12-23 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0002_profile_address_profile_description_profile_phone_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Complaint',
        ),
    ]
