# Generated by Django 5.1.1 on 2024-10-26 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ImageField(max_length=90, upload_to=''),
        ),
    ]
