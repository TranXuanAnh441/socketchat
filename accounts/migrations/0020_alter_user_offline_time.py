# Generated by Django 4.0.1 on 2022-01-09 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_friendrequest_sender_alter_user_offline_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='offline_time',
            field=models.TimeField(default=datetime.datetime(2022, 1, 9, 23, 19, 36, 813277)),
        ),
    ]
