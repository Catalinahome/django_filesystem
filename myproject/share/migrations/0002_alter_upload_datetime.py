# Generated by Django 4.0.4 on 2023-01-30 03:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 30, 11, 53, 28, 666002), verbose_name='上传时间'),
        ),
    ]
