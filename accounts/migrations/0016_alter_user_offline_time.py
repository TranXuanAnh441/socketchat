# Generated by Django 4.0 on 2022-01-08 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_notification_destination_alter_user_offline_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='offline_time',
            field=models.TimeField(default=datetime.datetime(2022, 1, 8, 13, 45, 51, 514925)),
        ),
    ]
