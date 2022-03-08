# Generated by Django 4.0.1 on 2022-01-23 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0029_evidence_linked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evidence',
            name='linked',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='evidence',
        ),
        migrations.AddField(
            model_name='evidence',
            name='linkd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crime.profile'),
        ),
    ]