# Generated by Django 5.1.1 on 2024-11-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_stat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Est',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media/')),
                ('nomi', models.CharField(max_length=90)),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=90)),
                ('text1', models.TextField()),
                ('name1', models.CharField(max_length=90)),
                ('text2', models.TextField()),
                ('name2', models.CharField(max_length=90)),
                ('text3', models.TextField()),
                ('name3', models.CharField(max_length=90)),
                ('text4', models.TextField()),
            ],
        ),
    ]
