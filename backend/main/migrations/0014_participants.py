# Generated by Django 5.0.1 on 2024-01-18 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_event_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='participants',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=124, null=True)),
            ],
        ),
    ]
