# Generated by Django 5.1.1 on 2024-10-27 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_service_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
