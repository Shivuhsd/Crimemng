# Generated by Django 4.0.1 on 2022-01-21 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0022_alter_profile_evidence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='evidence',
            field=models.FileField(null=True, upload_to='evidence/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fir',
            field=models.FileField(null=True, upload_to='fir/'),
        ),
    ]