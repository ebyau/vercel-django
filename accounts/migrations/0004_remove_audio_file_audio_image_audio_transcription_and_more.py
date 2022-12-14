# Generated by Django 4.1.3 on 2022-11-21 09:22

import cloudinary_storage.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_audio_date_created_alter_audio_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='file',
        ),
        migrations.AddField(
            model_name='audio',
            name='image',
            field=models.ImageField(null=True, upload_to='kin-keepers/audios', validators=[cloudinary_storage.validators.validate_video]),
        ),
        migrations.AddField(
            model_name='audio',
            name='transcription',
            field=models.ImageField(null=True, upload_to='kin-keepers/transcriptions/'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 9, 22, 18, 826595, tzinfo=datetime.timezone.utc)),
        ),
    ]
