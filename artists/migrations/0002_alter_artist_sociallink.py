# Generated by Django 4.1.2 on 2022-10-18 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='SocialLink',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]