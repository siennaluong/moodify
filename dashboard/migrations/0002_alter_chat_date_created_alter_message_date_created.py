# Generated by Django 4.1.1 on 2022-12-18 00:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 12, 18, 0, 12, 15, 217344)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 12, 18, 0, 12, 15, 217507)),
        ),
    ]
