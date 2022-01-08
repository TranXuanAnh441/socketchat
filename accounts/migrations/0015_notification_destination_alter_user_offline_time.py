# Generated by Django 4.0 on 2022-01-08 02:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_notification_unread_alter_user_offline_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='destination',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='offline_time',
            field=models.TimeField(default=datetime.datetime(2022, 1, 8, 11, 22, 33, 924089)),
        ),
    ]
