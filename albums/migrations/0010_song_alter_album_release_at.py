# Generated by Django 4.1.2 on 2022-10-21 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0009_alter_album_release_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(height_field=100, upload_to=None, width_field=100)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='release_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 21, 21, 19, 37, 579400)),
        ),
    ]