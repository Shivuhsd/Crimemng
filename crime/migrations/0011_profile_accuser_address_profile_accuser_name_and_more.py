# Generated by Django 4.0 on 2021-12-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0010_rename_firstname_profile_firstname1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='accuser_address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='accuser_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='accuser_phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='evidence',
            field=models.FileField(null=True, upload_to='evidence_docs/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='fir',
            field=models.FileField(null=True, upload_to='fir_documents/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='image_accuser',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pincode',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
