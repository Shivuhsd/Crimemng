# Generated by Django 4.0.1 on 2022-01-21 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0020_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='evidence',
            field=models.FileField(null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fir',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]
