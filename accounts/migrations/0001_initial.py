# Generated by Django 4.1.3 on 2022-11-16 11:39

import cloudinary_storage.storage
import cloudinary_storage.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 11, 16, 11, 39, 27, 777401, tzinfo=datetime.timezone.utc))),
                ('file', models.ImageField(null=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='videos/', validators=[cloudinary_storage.validators.validate_video])),
            ],
        ),
    ]
