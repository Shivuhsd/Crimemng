# Generated by Django 4.0.1 on 2022-01-29 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0054_evidences_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidences',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='crime.profile'),
        ),
    ]