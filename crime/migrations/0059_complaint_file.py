# Generated by Django 4.0.1 on 2022-02-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0058_evidencea_evidenced_evidencei_evidencev_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='file',
            field=models.FileField(blank=True, upload_to='complaintfile/'),
        ),
    ]