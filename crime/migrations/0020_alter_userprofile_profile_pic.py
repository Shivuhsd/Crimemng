# Generated by Django 4.0.1 on 2022-01-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0019_userprofile_address_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='images/profile'),
        ),
    ]
