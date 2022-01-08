# Generated by Django 4.0 on 2022-01-08 01:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_user_offline_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='offline_time',
            field=models.TimeField(default=datetime.datetime(2022, 1, 8, 10, 28, 31, 475874)),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('noti_type', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='accounts.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='accounts.user')),
            ],
        ),
    ]
