# Generated by Django 4.0 on 2022-01-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_message_filename_message_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
