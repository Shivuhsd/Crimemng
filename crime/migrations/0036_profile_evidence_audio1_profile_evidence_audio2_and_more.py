# Generated by Django 4.0.1 on 2022-01-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0035_profile_accuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='evidence_Audio1',
            field=models.FileField(blank=True, upload_to='evidence_audio/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='evidence_Audio2',
            field=models.FileField(blank=True, upload_to='evidence_audio/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='evidence_Documents1',
            field=models.FileField(blank=True, upload_to='evidence_doc/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='evidence_Documents2',
            field=models.FileField(blank=True, upload_to='evidence_doc/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='evidence_Video1',
            field=models.FileField(blank=True, upload_to='evidence_video/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='evidence_Video2',
            field=models.FileField(blank=True, upload_to='evidence_video/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='evidence_img',
            field=models.ImageField(blank=True, upload_to='evidence_img/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='evidence_Video',
            field=models.FileField(blank=True, upload_to='evidence_video/'),
        ),
    ]
