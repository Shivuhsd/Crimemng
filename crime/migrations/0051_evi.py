# Generated by Django 4.0.1 on 2022-01-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0050_alter_profile_evidence_audio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='imagetest/')),
            ],
        ),
    ]