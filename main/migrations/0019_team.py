# Generated by Django 5.1.1 on 2024-11-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_est'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media/')),
                ('ism', models.CharField(max_length=90)),
                ('ish', models.CharField(max_length=90)),
                ('text', models.TextField()),
            ],
        ),
    ]
