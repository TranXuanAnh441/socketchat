# Generated by Django 4.0 on 2021-12-31 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_merge_20211231_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='offline_time',
            field=models.TimeField(default=datetime.datetime(2021, 12, 31, 19, 31, 11, 450475)),
        ),
    ]
