# Generated by Django 4.0.1 on 2022-01-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0018_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
