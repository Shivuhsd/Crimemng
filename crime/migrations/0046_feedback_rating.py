# Generated by Django 4.0.1 on 2022-01-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0045_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='rating',
            field=models.TextField(max_length=1, null=True),
        ),
    ]