# Generated by Django 5.0.1 on 2024-01-19 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_participants_events_alter_participants_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='participants',
            new_name='participant',
        ),
    ]
