# Generated by Django 5.1.1 on 2024-10-29 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_enim'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enim',
            name='nomi',
        ),
        migrations.RemoveField(
            model_name='enim',
            name='text',
        ),
    ]
