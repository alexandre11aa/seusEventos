# Generated by Django 5.0.1 on 2024-01-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='banner',
            field=models.ImageField(upload_to='main/image/'),
        ),
    ]