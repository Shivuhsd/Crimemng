# Generated by Django 4.0.1 on 2022-01-21 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0021_alter_profile_evidence_alter_profile_fir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='evidence',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]