# Generated by Django 3.1.7 on 2023-04-17 11:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0002_auto_20230417_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='time_of_recording',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 11, 46, 51, 241013, tzinfo=utc)),
        ),
    ]