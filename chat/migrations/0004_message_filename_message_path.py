# Generated by Django 4.0 on 2022-01-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='filename',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='path',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
