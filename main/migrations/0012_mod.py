# Generated by Django 5.1.1 on 2024-10-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_enim_nomi_remove_enim_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=90)),
                ('name', models.CharField(max_length=90)),
                ('text', models.TextField()),
                ('text1', models.TextField()),
                ('text2', models.TextField()),
                ('text3', models.TextField()),
                ('rasm', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
