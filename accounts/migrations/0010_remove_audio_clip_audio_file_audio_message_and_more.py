# Generated by Django 4.1.3 on 2022-11-21 11:10

import cloudinary.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_audio_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='clip',
        ),
        migrations.AddField(
            model_name='audio',
            name='file',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='audio',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='audio',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 11, 10, 8, 166829, tzinfo=datetime.timezone.utc)),
        ),
    ]
